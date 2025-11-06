from experta import Rule, KnowledgeEngine, MATCH 
from controller import converFact_to_string, response, generate_explanation
from facts import knowledge_base, ApartmentFact, PRICE_RANGES
import math

class ApartmentAdvisorSystem(KnowledgeEngine):
    def __init__(self, knowledge_base):
        super().__init__()
        self.knowledge_base = knowledge_base
        self.inferred_apartments = []
        self.alternatives = []
        self.user_preferences = {}
    
    @Rule(
        ApartmentFact(
            location=MATCH.location,
            developer=MATCH.developer,
            price_range=MATCH.price_range,
            apartment_type=MATCH.apartment_type,
            bedrooms=MATCH.bedrooms,
            bathrooms=MATCH.bathrooms,
            amenities=MATCH.amenities,
            rating=MATCH.rating,
            floor_number=MATCH.floor_number  
        ),
        salience=10,
    )
    def exact_match(self, location, developer, price_range, apartment_type, bedrooms, bathrooms, amenities, rating, floor_number):  # Add floor_number parameter
        self.user_preferences.update({
            'location': location, 'developer': developer, 'price_range': price_range,
            'apartment_type': apartment_type, 'bedrooms': bedrooms, 'bathrooms': bathrooms,
            'amenities': amenities, 'rating': rating, 'floor_number': floor_number  # Add this line
        })
        
        self.inferred_apartments = []
        for apt in self.knowledge_base:
            matches = (
                (not location or location in ["", "any", "no preference"] or apt["location"].lower() == location.lower()) and
                (not developer or developer in ["", "any", "no preference"] or apt["developer"].lower() == developer.lower()) and
                (not price_range or price_range in ["", "any", "no preference"] or apt["price_range"].lower() == price_range.lower()) and
                (not apartment_type or apartment_type in ["", "any", "no preference"] or apt["apartment_type"].lower() == apartment_type.lower()) and
                (not bedrooms or bedrooms in ["", "any", "no preference"] or apt["bedrooms"] == bedrooms) and
                (not bathrooms or bathrooms in ["", "any", "no preference"] or apt["bathrooms"] == bathrooms) and
                (not amenities or len(amenities) == 0 or len({i.lower() for i in apt["amenities"]}.intersection({j.lower() for j in amenities})) > 0) and
                (not rating or rating == 0 or apt["rating"] >= rating) and
                (not floor_number or not isinstance(floor_number, (int, float)) or floor_number == 0 or apt["floor_number"] >= floor_number)  # Floor matching
            )
            
            if matches:
                self.inferred_apartments.append(converFact_to_string(apt))
        
        if self.inferred_apartments:
            explanations = []
            for apt in self.inferred_apartments:
                explanation = generate_explanation(apt, self.user_preferences, 100)
                explanations.append({
                    'apartment': apt['title'],
                    'explanation': explanation
                })
            
            response.update({
                "response_message": "🎉 Perfect matches found! Here are apartments that exactly match your criteria:",
                "response_data": self.inferred_apartments,
                "explanations": explanations
            })

    @Rule(
        ApartmentFact(
            amenities=MATCH.amenities,
            location=MATCH.location,
            developer=MATCH.developer,
            price_range=MATCH.price_range,
            apartment_type=MATCH.apartment_type,
            bedrooms=MATCH.bedrooms,
            bathrooms=MATCH.bathrooms,
            rating=MATCH.rating,
            floor_number=MATCH.floor_number  
        ),
        salience=7,
    )
    def suggest_alternatives(self, amenities, location, developer, price_range, apartment_type, bedrooms, bathrooms, rating, floor_number):
        self.user_preferences.update({
            'location': location, 'developer': developer, 'price_range': price_range,
            'apartment_type': apartment_type, 'bedrooms': bedrooms, 'bathrooms': bathrooms,
            'amenities': amenities, 'rating': rating, 'floor_number': floor_number
        })
        
        self.alternatives = []
        explanations = []
        null_values_list = []
                                            
        if not self.inferred_apartments:
            if not location or location in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("location")
            if not developer or developer in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("developer")
            if not price_range or price_range in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("price range")
            if not apartment_type or apartment_type in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("apartment type")
            if not bedrooms or bedrooms in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("bedrooms")
            if not bathrooms or bathrooms in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("bathrooms")
            if not rating or rating in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("rating")
            if not floor_number or floor_number in ["no idea", "anything", "any", "no preference", "no specific", ""]:
                null_values_list.append("floor number")
            if not amenities or any(amenity in ["no idea", "anything", "any", "no preference", "no specific", ""] for amenity in amenities):
                null_values_list.append("amenities")
             
            totalMarks = len(amenities) + 20
            for apartment in self.knowledge_base:
                relevance_score = 0
                
                if amenities and len(amenities) > 0:
                    relevance_score += len(apartment["amenities"].intersection(amenities))
                
                if rating and rating > 0 and apartment["rating"] >= rating:
                    relevance_score += 2
                
                if location and location not in ["", "any", "no preference"] and apartment["location"].lower() == location.lower():
                    relevance_score += 6
                if developer and developer not in ["", "any", "no preference"] and apartment["developer"].lower() == developer.lower():
                    relevance_score += 4
                if price_range and price_range not in ["", "any", "no preference"] and apartment["price_range"].lower() == price_range.lower():
                    relevance_score += 5
                if apartment_type and apartment_type not in ["", "any", "no preference"] and apartment["apartment_type"].lower() == apartment_type.lower():
                    relevance_score += 4
                if bedrooms and bedrooms not in ["", "any", "no preference"] and apartment["bedrooms"] == bedrooms:
                    relevance_score += 3
                if bathrooms and bathrooms not in ["", "any", "no preference"] and apartment["bathrooms"] == bathrooms:
                    relevance_score += 2
                
                if floor_number and isinstance(floor_number, (int, float)) and floor_number > 0:
                    if apartment["floor_number"] == floor_number:
                        relevance_score += 3 
                    elif apartment["floor_number"] > 0:  
                        relevance_score += 1  
                
                if relevance_score > 0:
                    score = math.floor((relevance_score / totalMarks) * 100) if totalMarks > 0 else 50
                    apt_data = converFact_to_string(apartment)
                    explanation = generate_explanation(apartment, self.user_preferences, score)
                    self.alternatives.append((apt_data, score, explanation))
            
            self.alternatives.sort(key=lambda x: x[1], reverse=True)

            if null_values_list:
                String_value = " , ".join(map(str, null_values_list))
                if not self.alternatives:
                    popular_apartments = sorted(knowledge_base, key=lambda x: x['rating'], reverse=True)[:5]
                    self.alternatives = [(converFact_to_string(apt), 50, "Popular high-rated apartment in Colombo") for apt in popular_apartments]
                    
                    response.update({
                        "response_message": "🤔 You haven't specified strong preferences. Here are some popular apartments in Colombo that might interest you:",
                        "response_data": self.alternatives,
                        "explanations": [{'apartment': apt_data['title'], 'explanation': explanation} for apt_data, score, explanation in self.alternatives]
                    })
                else: 
                    num_of_apartments = min(5, len(self.alternatives))
                    response.update({
                        "response_message": f"💡 Based on your preferences (though you weren't specific about {String_value}), here are some great options:",
                        "response_data": self.alternatives[:num_of_apartments],
                        "explanations": [{'apartment': apt_data['title'], 'explanation': explanation} for apt_data, score, explanation in self.alternatives[:num_of_apartments]]
                    })
            else:
                num_of_apartments = min(5, len(self.alternatives))
                if self.alternatives:
                    _, percentage, _ = self.alternatives[0]
                    if percentage >= 90:
                        response.update({
                            "response_message": "🎯 Excellent matches found! These apartments closely match all your criteria:",
                            "response_data": self.alternatives[:num_of_apartments],
                            "explanations": [{'apartment': apt_data['title'], 'explanation': explanation} for apt_data, score, explanation in self.alternatives[:num_of_apartments]]
                        })
                    else:     
                        response.update({
                            "response_message": "📋 Good alternatives found! While not perfect matches, these apartments meet most of your criteria:",
                            "response_data": self.alternatives[:num_of_apartments],
                            "explanations": [{'apartment': apt_data['title'], 'explanation': explanation} for apt_data, score, explanation in self.alternatives[:num_of_apartments]]
                        })
                else:
                    popular_apartments = sorted(knowledge_base, key=lambda x: x['rating'], reverse=True)[:3]
                    self.alternatives = [(converFact_to_string(apt), 40, "Highly rated alternative that might interest you") for apt in popular_apartments]
                    response.update({
                        "response_message": "🔍 No exact matches found with your specific criteria. Here are some highly-rated alternatives:",
                        "response_data": self.alternatives,
                        "explanations": [{'apartment': apt_data['title'], 'explanation': explanation} for apt_data, score, explanation in self.alternatives]
                    })