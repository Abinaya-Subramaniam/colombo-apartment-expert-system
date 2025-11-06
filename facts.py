from experta import Fact

class ApartmentFact(Fact):
    title = str
    location = str
    developer = str
    price = float 
    price_range = str
    apartment_type = str
    bedrooms = int
    bathrooms = int
    area_sqft = float
    amenities = set
    rating = float
    completion_year = int
    floor_number = int  

    def __str__(self):
        return (f"Title: {self.title}, Location: {self.location}, Developer: {self.developer}, "
                f"Price: {self.price}, Type: {self.apartment_type}, "
                f"Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, "
                f"Area: {self.area_sqft} sqft, Rating: {self.rating}, Floor: {self.floor_number}")  
    
knowledge_base = [
    ApartmentFact(title="Marino Mall Residences", location="Colombo 3", developer="Altair Group",
                 amenities={"swimming pool", "gym", "parking", "security", "elevator", "concierge"}, 
                 rating=4.5, price=85000000, price_range="High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1800, completion_year=2023, floor_number=15),
    
    ApartmentFact(title="Havelock City", location="Colombo 5", developer="Overseas Realty",
                 amenities={"swimming pool", "gym", "parking", "security", "garden", "playground", "clubhouse"}, 
                 rating=4.7, price=75000000, price_range="High", apartment_type="Luxury", 
                 bedrooms=2, bathrooms=2, area_sqft=1500, completion_year=2022, floor_number=8),
    
    ApartmentFact(title="Crescat Boulevard", location="Colombo 3", developer="Crescat Development",
                 amenities={"swimming pool", "gym", "parking", "security", "shopping mall", "concierge"}, 
                 rating=4.8, price=120000000, price_range="Premium", apartment_type="Ultra Luxury", 
                 bedrooms=4, bathrooms=3, area_sqft=2200, completion_year=2024, floor_number=25),
    
    ApartmentFact(title="Mireka Towers", location="Colombo 2", developer="Mireka Capital Land",
                 amenities={"gym", "parking", "security", "elevator"}, 
                 rating=4.2, price=35000000, price_range="Medium", apartment_type="Standard", 
                 bedrooms=2, bathrooms=1, area_sqft=1200, completion_year=2021, floor_number=5),
    
    ApartmentFact(title="Empire Apartments", location="Colombo 7", developer="Empire Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "concierge", "garden"}, 
                 rating=4.6, price=68000000, price_range="High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1700, completion_year=2023, floor_number=12),
    
    ApartmentFact(title="Green City Residence", location="Colombo 5", developer="Green Builders",
                 amenities={"garden", "parking", "security", "playground", "solar panels"}, 
                 rating=4.3, price=42000000, price_range="Medium", apartment_type="Eco-Friendly", 
                 bedrooms=2, bathrooms=1, area_sqft=1350, completion_year=2022, floor_number=3),
    
    ApartmentFact(title="Ocean View Apartments", location="Colombo 4", developer="Seaside Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "sea view", "balcony"}, 
                 rating=4.4, price=55000000, price_range="Medium-High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1600, completion_year=2023, floor_number=18),
    
    ApartmentFact(title="Business Tower Residences", location="Colombo 1", developer="Commercial Developers",
                 amenities={"gym", "parking", "security", "business center", "conference room"}, 
                 rating=4.5, price=72000000, price_range="High", apartment_type="Commercial", 
                 bedrooms=2, bathrooms=2, area_sqft=1400, completion_year=2024, floor_number=22),
    
    ApartmentFact(title="Sky Gardens", location="Colombo 3", developer="Skyline Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "rooftop garden", "jacuzzi"}, 
                 rating=4.7, price=95000000, price_range="Premium", apartment_type="Penthouse", 
                 bedrooms=4, bathrooms=3, area_sqft=2400, completion_year=2024, floor_number=30),
    
    ApartmentFact(title="Metro Apartments", location="Colombo 2", developer="Metro Builders",
                 amenities={"gym", "parking", "security", "elevator"}, 
                 rating=4.1, price=28000000, price_range="Low-Medium", apartment_type="Standard", 
                 bedrooms=1, bathrooms=1, area_sqft=850, completion_year=2020, floor_number=4),
    
    ApartmentFact(title="Royal Park Residence", location="Colombo 7", developer="Royal Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "park view", "concierge"}, 
                 rating=4.8, price=110000000, price_range="Premium", apartment_type="Luxury", 
                 bedrooms=4, bathrooms=3, area_sqft=2100, completion_year=2023, floor_number=20),
    
    ApartmentFact(title="Budget Homes", location="Colombo 8", developer="Budget Developers",
                 amenities={"parking", "security", "elevator"}, 
                 rating=3.9, price=18000000, price_range="Low", apartment_type="Economy", 
                 bedrooms=1, bathrooms=1, area_sqft=750, completion_year=2019, floor_number=2),
    
    ApartmentFact(title="Executive Suites", location="Colombo 1", developer="Executive Developers",
                 amenities={"gym", "parking", "security", "business center", "concierge"}, 
                 rating=4.7, price=65000000, price_range="High", apartment_type="Executive", 
                 bedrooms=2, bathrooms=2, area_sqft=1350, completion_year=2023, floor_number=16),
    
    ApartmentFact(title="Tech Park Residences", location="Colombo 5", developer="Tech Developers",
                 amenities={"gym", "parking", "security", "high-speed internet", "co-working space"}, 
                 rating=4.5, price=58000000, price_range="High", apartment_type="Modern", 
                 bedrooms=2, bathrooms=2, area_sqft=1400, completion_year=2024, floor_number=14),
    
    ApartmentFact(title="Beachside Residences", location="Colombo 4", developer="Beachfront Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "private beach", "spa"}, 
                 rating=4.9, price=150000000, price_range="Premium", apartment_type="Ultra Luxury", 
                 bedrooms=3, bathrooms=3, area_sqft=1900, completion_year=2024, floor_number=28),

    # Additional 15 apartments to make total 30
    ApartmentFact(title="Liberty Plaza Apartments", location="Colombo 3", developer="Liberty Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "concierge", "library"}, 
                 rating=4.4, price=62000000, price_range="Medium-High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1650, completion_year=2022, floor_number=10),
    
    ApartmentFact(title="Garden City Residences", location="Colombo 7", developer="Garden City Developers",
                 amenities={"garden", "parking", "security", "playground", "community hall"}, 
                 rating=4.2, price=38000000, price_range="Medium", apartment_type="Family", 
                 bedrooms=2, bathrooms=2, area_sqft=1250, completion_year=2021, floor_number=6),
    
    ApartmentFact(title="Capital Towers", location="Colombo 1", developer="Capital Builders",
                 amenities={"gym", "parking", "security", "business center", "elevator"}, 
                 rating=4.3, price=48000000, price_range="Medium", apartment_type="Commercial", 
                 bedrooms=2, bathrooms=1, area_sqft=1100, completion_year=2020, floor_number=12),
    
    ApartmentFact(title="Lake View Apartments", location="Colombo 5", developer="Lakeview Developers",
                 amenities={"swimming pool", "parking", "security", "lake view", "balcony"}, 
                 rating=4.6, price=78000000, price_range="High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1750, completion_year=2023, floor_number=17),
    
    ApartmentFact(title="City Center Lofts", location="Colombo 2", developer="Urban Developers",
                 amenities={"gym", "parking", "security", "rooftop terrace", "elevator"}, 
                 rating=4.0, price=32000000, price_range="Low-Medium", apartment_type="Studio", 
                 bedrooms=1, bathrooms=1, area_sqft=900, completion_year=2021, floor_number=7),
    
    ApartmentFact(title="Pearl Bay Residences", location="Colombo 4", developer="Pearl Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "sea view", "jacuzzi"}, 
                 rating=4.7, price=88000000, price_range="High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1850, completion_year=2024, floor_number=24),
    
    ApartmentFact(title="Heritage Homes", location="Colombo 7", developer="Heritage Builders",
                 amenities={"garden", "parking", "security", "historical architecture", "library"}, 
                 rating=4.5, price=52000000, price_range="Medium", apartment_type="Heritage", 
                 bedrooms=2, bathrooms=1, area_sqft=1300, completion_year=2018, floor_number=3),
    
    ApartmentFact(title="Sunrise Apartments", location="Colombo 6", developer="Sunrise Developers",
                 amenities={"parking", "security", "garden", "playground"}, 
                 rating=4.1, price=25000000, price_range="Low-Medium", apartment_type="Standard", 
                 bedrooms=2, bathrooms=1, area_sqft=1000, completion_year=2019, floor_number=4),
    
    ApartmentFact(title="Platinum Towers", location="Colombo 3", developer="Platinum Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "concierge", "spa", "cinema"}, 
                 rating=4.8, price=135000000, price_range="Premium", apartment_type="Ultra Luxury", 
                 bedrooms=4, bathrooms=3, area_sqft=2300, completion_year=2024, floor_number=26),
    
    ApartmentFact(title="Urban Nest Apartments", location="Colombo 5", developer="Urban Nest Developers",
                 amenities={"gym", "parking", "security", "co-working space", "cafe"}, 
                 rating=4.2, price=45000000, price_range="Medium", apartment_type="Modern", 
                 bedrooms=1, bathrooms=1, area_sqft=950, completion_year=2022, floor_number=9),
    
    ApartmentFact(title="Mountain View Residences", location="Colombo 7", developer="Mountain View Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "mountain view", "terrace"}, 
                 rating=4.6, price=72000000, price_range="High", apartment_type="Luxury", 
                 bedrooms=3, bathrooms=2, area_sqft=1680, completion_year=2023, floor_number=15),
    
    ApartmentFact(title="Eco Living Apartments", location="Colombo 8", developer="Eco Developers",
                 amenities={"garden", "parking", "security", "solar panels", "rainwater harvesting"}, 
                 rating=4.3, price=35000000, price_range="Medium", apartment_type="Eco-Friendly", 
                 bedrooms=2, bathrooms=1, area_sqft=1150, completion_year=2022, floor_number=5),
    
    ApartmentFact(title="Business Hub Residences", location="Colombo 1", developer="Business Hub Developers",
                 amenities={"gym", "parking", "security", "business center", "conference rooms"}, 
                 rating=4.4, price=68000000, price_range="High", apartment_type="Executive", 
                 bedrooms=2, bathrooms=2, area_sqft=1450, completion_year=2023, floor_number=18),
    
    ApartmentFact(title="Family Friendly Homes", location="Colombo 6", developer="Family Developers",
                 amenities={"playground", "parking", "security", "garden", "community center"}, 
                 rating=4.2, price=30000000, price_range="Low-Medium", apartment_type="Family", 
                 bedrooms=3, bathrooms=2, area_sqft=1400, completion_year=2020, floor_number=4),
    
    ApartmentFact(title="Luxury Penthouses", location="Colombo 3", developer="Luxury Living Developers",
                 amenities={"swimming pool", "gym", "parking", "security", "private terrace", "jacuzzi", "concierge"}, 
                 rating=4.9, price=160000000, price_range="Premium", apartment_type="Penthouse", 
                 bedrooms=4, bathrooms=3, area_sqft=2500, completion_year=2024, floor_number=32),
    
    ApartmentFact(title="Comfort Living Apartments", location="Colombo 6", developer="Comfort Builders",
             amenities={"parking", "security", "garden", "elevator"}, 
             rating=4.0, price=28000000, price_range="Low-Medium", apartment_type="Standard", 
             bedrooms=2, bathrooms=1, area_sqft=1100, completion_year=2020, floor_number=5),

ApartmentFact(title="City View Homes", location="Colombo 8", developer="City View Developers",
             amenities={"parking", "security", "elevator", "balcony"}, 
             rating=3.9, price=22000000, price_range="Low", apartment_type="Economy", 
             bedrooms=1, bathrooms=1, area_sqft=800, completion_year=2019, floor_number=3),

ApartmentFact(title="Green Valley Residences", location="Colombo 5", developer="Green Valley Builders",
             amenities={"garden", "parking", "security", "playground"}, 
             rating=4.1, price=25000000, price_range="Low-Medium", apartment_type="Eco-Friendly", 
             bedrooms=2, bathrooms=1, area_sqft=1050, completion_year=2021, floor_number=4),

ApartmentFact(title="Modern Studio Apartments", location="Colombo 2", developer="Modern Living",
             amenities={"parking", "security", "elevator", "high-speed internet"}, 
             rating=4.2, price=19000000, price_range="Low", apartment_type="Studio", 
             bedrooms=1, bathrooms=1, area_sqft=700, completion_year=2022, floor_number=6),

ApartmentFact(title="Family Comfort Homes", location="Colombo 6", developer="Family Comfort Developers",
             amenities={"parking", "security", "playground", "community hall"}, 
             rating=4.0, price=27000000, price_range="Low-Medium", apartment_type="Family", 
             bedrooms=2, bathrooms=2, area_sqft=1200, completion_year=2020, floor_number=4),

ApartmentFact(title="Urban Studio Lofts", location="Colombo 4", developer="Urban Studio",
             amenities={"parking", "security", "elevator", "rooftop access"}, 
             rating=4.1, price=23000000, price_range="Low-Medium", apartment_type="Studio", 
             bedrooms=1, bathrooms=1, area_sqft=750, completion_year=2021, floor_number=7),

ApartmentFact(title="Budget Friendly Residences", location="Colombo 8", developer="Budget Friendly Developers",
             amenities={"parking", "security"}, 
             rating=3.8, price=15000000, price_range="Low", apartment_type="Economy", 
             bedrooms=1, bathrooms=1, area_sqft=650, completion_year=2018, floor_number=2),

ApartmentFact(title="Comfort Zone Apartments", location="Colombo 6", developer="Comfort Zone Builders",
             amenities={"parking", "security", "garden", "elevator", "community space"}, 
             rating=4.0, price=26000000, price_range="Low-Medium", apartment_type="Standard", 
             bedrooms=2, bathrooms=1, area_sqft=1150, completion_year=2021, floor_number=5),

ApartmentFact(title="Smart Living Studios", location="Colombo 2", developer="Smart Living Developers",
             amenities={"parking", "security", "high-speed internet", "elevator"}, 
             rating=4.2, price=21000000, price_range="Low-Medium", apartment_type="Modern", 
             bedrooms=1, bathrooms=1, area_sqft=720, completion_year=2022, floor_number=8),

ApartmentFact(title="Garden View Homes", location="Colombo 5", developer="Garden View Developers",
             amenities={"garden", "parking", "security", "playground", "community area"}, 
             rating=4.1, price=24000000, price_range="Low-Medium", apartment_type="Family", 
             bedrooms=2, bathrooms=1, area_sqft=1080, completion_year=2020, floor_number=3),
]

PRICE_RANGES = {
    "Low": "Under Rs. 2 Crores",
    "Low-Medium": "Rs. 2-4 Crores", 
    "Medium": "Rs. 4-6 Crores",
    "Medium-High": "Rs. 6-8 Crores",
    "High": "Rs. 8-10 Crores",
    "Premium": "Over Rs. 10 Crores"
}