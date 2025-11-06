def converFact_to_string(fact):
    return {
        "title": fact['title'],
        "location": fact['location'],
        "developer": fact['developer'],
        "price": fact['price'],
        "price_range": fact['price_range'],
        "apartment_type": fact['apartment_type'],
        "bedrooms": fact['bedrooms'],
        "bathrooms": fact['bathrooms'],
        "area_sqft": fact['area_sqft'],
        "amenities": fact['amenities'],
        "rating": fact['rating'],
        "completion_year": fact['completion_year'],
        "floor_number": fact['floor_number'] 
    }

response = {
    "response_message": "",
    "response_data": [],
    "explanations": []
}

def format_price(price_lkr):
    """Convert LKR price to readable format (Crores/Lakhs)"""
    if price_lkr >= 10000000: 
        return f"Rs. {price_lkr/10000000:.2f} Crores"
    elif price_lkr >= 100000:  
        return f"Rs. {price_lkr/100000:.2f} Lakhs"
    else:
        return f"Rs. {price_lkr:,}"

def get_apartment_display(apartment: dict, score=None, explanation=None):
    display = f"""
### 🏢 {apartment.get('title', 'Unknown Title')} 
{f"**Match Score: {score}%**" if score else ""}

**📍 Location:** {apartment.get('location', 'Unknown Location')}  
**🏗️ Developer:** {apartment.get('developer', 'Unknown Developer')}  
**💰 Price:** {format_price(apartment.get('price', 0))}  
**🎯 Type:** {apartment.get('apartment_type', 'N/A')}  
**🛏️ Bedrooms:** {apartment.get('bedrooms', 'N/A')}  
**🚿 Bathrooms:** {apartment.get('bathrooms', 'N/A')}  
**📐 Area:** {apartment.get('area_sqft', 'N/A'):,} sqft  
**🏢 Floor:** {apartment.get('floor_number', 'N/A')}  # Add this line
**⭐ Rating:** {apartment.get('rating', 'N/A')}/5  
**📅 Year:** {apartment.get('completion_year', 'N/A')}  
**🏊 Amenities:** {', '.join(apartment.get('amenities', []))}
"""
    
    if explanation:
        display += f"\n**🤔 Why this match:** {explanation}"
    
    return display

def generate_explanation(apartment, user_prefs, score):
    explanations = []
    
    if user_prefs.get('location') and apartment['location'].lower() == user_prefs['location'].lower():
        explanations.append(f"Perfect location match in {apartment['location']}")
    
    if user_prefs.get('price_range') and apartment['price_range'].lower() == user_prefs['price_range'].lower():
        explanations.append(f"Fits your {apartment['price_range']} budget range")
    
    user_amenities = user_prefs.get('amenities', set())
    matched_amenities = user_amenities.intersection(apartment['amenities'])
    if matched_amenities:
        explanations.append(f"Has your preferred amenities: {', '.join(matched_amenities)}")
    
    if user_prefs.get('bedrooms') and apartment['bedrooms'] == user_prefs['bedrooms']:
        explanations.append(f"Exactly {apartment['bedrooms']} bedrooms as requested")
    
    user_floor = user_prefs.get('floor_number')
    apartment_floor = apartment.get('floor_number', 0)
    
    try:
        if isinstance(user_floor, str) and user_floor.isdigit():
            user_floor = int(user_floor)
        if isinstance(apartment_floor, str) and apartment_floor.isdigit():
            apartment_floor = int(apartment_floor)
    except (ValueError, AttributeError):
        pass
    
    if user_floor and user_floor > 0:
        if apartment_floor == user_floor:
            explanations.append(f"Perfect floor match on floor {apartment['floor_number']}")
        elif apartment_floor > user_floor:
            explanations.append(f"Higher floor ({apartment['floor_number']}) - better views")
        else:
            explanations.append(f"Lower floor ({apartment['floor_number']}) - elevator-independent access")
    
    if user_prefs.get('rating') and apartment['rating'] >= user_prefs['rating']:
        explanations.append(f"High rating of {apartment['rating']}/5 meets your standards")
    
    if user_prefs.get('developer') and apartment['developer'].lower() == user_prefs['developer'].lower():
        explanations.append(f"From your preferred developer {apartment['developer']}")
    
    if user_prefs.get('apartment_type') and apartment['apartment_type'].lower() == user_prefs['apartment_type'].lower():
        explanations.append(f"Matches your preferred {apartment['apartment_type']} type")
    
    if not explanations:
        explanations.append(f"Good overall match based on your preferences with {score}% compatibility")
    
    return " • ".join(explanations)

def explain_price_ranges():
    return """
**💰 Price Range Guide for Colombo Apartments:**

• **Low**: Under Rs. 2 Crores (Budget-friendly options)
• **Low-Medium**: Rs. 2-4 Crores (Good value apartments)  
• **Medium**: Rs. 4-6 Crores (Mid-range quality)
• **Medium-High**: Rs. 6-8 Crores (Premium living)
• **High**: Rs. 8-10 Crores (Luxury apartments)
• **Premium**: Over Rs. 10 Crores (Ultra-luxury penthouses)
"""