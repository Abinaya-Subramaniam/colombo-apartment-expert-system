import streamlit as st
from experta import Fact
from controller import converFact_to_string, response, get_apartment_display, format_price, explain_price_ranges
from facts import knowledge_base, ApartmentFact, PRICE_RANGES
from main import ApartmentAdvisorSystem
import time

st.set_page_config(
    page_title="Colombo Apartment Advisor", 
    layout="wide", 
    page_icon="🏢",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(-45deg, #0F172A, #1E293B, #1a1f3a, #0F172A);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .hero-header {
        text-align: center;
        padding: 3rem 1rem;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 40px rgba(102, 126, 234, 0.3);
    }
    
    @keyframes textGlow {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.3); }
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #94A3B8;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border-right: 1px solid #334155;
    }
    
    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }
    
    .info-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.9));
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid rgba(99, 102, 241, 0.2);
        margin: 1rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .info-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(99, 102, 241, 0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.6s;
    }
    
    .info-card:hover::before {
        left: 100%;
    }
    
    .info-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(99, 102, 241, 0.5);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
    }
    
    .question-card {
        background: linear-gradient(135deg, #334155 0%, #475569 100%);
        padding: 2.5rem;
        border-radius: 25px;
        border-left: 6px solid #6366F1;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
        animation: slideInUp 0.5s ease-out;
        position: relative;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .question-number {
        position: absolute;
        top: -15px;
        left: 30px;
        background: linear-gradient(135deg, #6366F1, #8B5CF6);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 5px 20px rgba(99, 102, 241, 0.4);
    }
    
    .question-text {
        color: #F1F5F9;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        padding-top: 0.5rem;
    }
    
    .question-hint {
        color: #94A3B8;
        font-size: 1rem;
        font-style: italic;
        margin-bottom: 1.5rem;
    }
    
    .stTextInput input, .stSelectbox select {
        background: rgba(51, 65, 85, 0.8) !important;
        border: 2px solid #475569 !important;
        border-radius: 15px !important;
        color: #F1F5F9 !important;
        padding: 1rem 1.5rem !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput input:focus, .stSelectbox select:focus {
        border-color: #6366F1 !important;
        box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.2) !important;
        background: rgba(51, 65, 85, 1) !important;
        transform: scale(1.02);
    }
    
    .stButton button {
        background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 15px;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.6);
    }
    
    .stButton button:active {
        transform: translateY(-1px) scale(1.02);
    }
    
    .progress-container {
        margin: 2rem 0;
        padding: 1.5rem;
        background: rgba(30, 41, 59, 0.6);
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }
    
    .progress-bar {
        background: #334155;
        height: 12px;
        border-radius: 15px;
        overflow: hidden;
        position: relative;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #6366F1, #8B5CF6, #10B981);
        background-size: 200% 100%;
        border-radius: 15px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        animation: progressShine 2s ease infinite;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.6);
    }
    
    @keyframes progressShine {
        0% { background-position: 0% 0%; }
        100% { background-position: 200% 0%; }
    }
    
    .apartment-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.95) 0%, rgba(51, 65, 85, 0.95) 100%);
        padding: 2.5rem;
        border-radius: 25px;
        border: 1px solid rgba(99, 102, 241, 0.3);
        margin: 1.5rem 0;
        box-shadow: 0 15px 50px rgba(0,0,0,0.4);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .apartment-card::after {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.1), transparent);
        transition: all 0.8s;
    }
    
    .apartment-card:hover::after {
        top: -20%;
        right: -20%;
    }
    
    .apartment-card:hover {
        transform: translateY(-10px) rotateX(2deg);
        border-color: rgba(99, 102, 241, 0.6);
        box-shadow: 0 25px 80px rgba(99, 102, 241, 0.4);
    }
    
    .match-score {
        background: linear-gradient(135deg, #10B981, #059669);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 30px;
        font-weight: 800;
        display: inline-block;
        font-size: 1rem;
        box-shadow: 0 6px 25px rgba(16, 185, 129, 0.4);
        animation: scorePulse 2s ease infinite;
    }
    
    @keyframes scorePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .price-highlight {
        font-size: 1.6rem;
        font-weight: 900;
        background: linear-gradient(135deg, #F59E0B, #D97706, #F59E0B);
        background-size: 200% 100%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: priceShimmer 3s ease infinite;
        display: inline-block;
    }
    
    @keyframes priceShimmer {
        0%, 100% { background-position: 0% 0%; }
        50% { background-position: 200% 0%; }
    }
    
    .stChatMessage {
        padding: 1.5rem;
        border-radius: 20px;
        margin: 1rem 0;
        animation: messageSlide 0.4s ease-out;
        backdrop-filter: blur(10px);
    }
    
    @keyframes messageSlide {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .stChatMessage[data-testid*="user"] {
        background: linear-gradient(135deg, rgba(51, 65, 85, 0.8), rgba(71, 85, 105, 0.8));
        border-left: 4px solid #6366F1;
    }
    
    .stChatMessage[data-testid*="assistant"] {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(51, 65, 85, 0.8));
        border-left: 4px solid #10B981;
    }
    
    @keyframes successBounce {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.1); }
        50% { transform: scale(0.95); }
        75% { transform: scale(1.05); }
    }
    
    .success-icon {
        animation: successBounce 0.8s ease;
        display: inline-block;
        font-size: 3rem;
    }
    
    [data-testid="stTooltipIcon"] {
        color: #6366F1;
    }
    
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(51, 65, 85, 0.9), rgba(71, 85, 105, 0.9)) !important;
        border-radius: 15px !important;
        border: 1px solid #475569 !important;
        padding: 1.2rem 1.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #6366F1 !important;
        box-shadow: 0 5px 20px rgba(99, 102, 241, 0.3) !important;
    }
    
    .stSpinner > div {
        border-color: #6366F1 transparent #8B5CF6 transparent !important;
    }
    
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1E293B;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #6366F1, #8B5CF6);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #8B5CF6, #6366F1);
    }
    
    .badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        margin: 0.3rem;
        transition: all 0.3s ease;
    }
    
    .badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .badge-primary { 
        background: linear-gradient(135deg, #6366F1, #8B5CF6); 
        color: white; 
    }
    
    .badge-success { 
        background: linear-gradient(135deg, #10B981, #059669); 
        color: white; 
    }
    
    .badge-warning { 
        background: linear-gradient(135deg, #F59E0B, #D97706); 
        color: white; 
    }
    
    .area-badge {
        background: rgba(51, 65, 85, 0.6);
        padding: 0.8rem 1rem;
        border-radius: 12px;
        margin: 0.4rem 0;
        border-left: 3px solid #6366F1;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }
    
    .area-badge:hover {
        background: rgba(99, 102, 241, 0.2);
        border-left-width: 5px;
        transform: translateX(5px);
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
        border: 2px solid rgba(99, 102, 241, 0.3);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .skip-button {
        background: transparent !important;
        border: 2px solid #475569 !important;
        color: #94A3B8 !important;
    }
    
    .skip-button:hover {
        background: rgba(71, 85, 105, 0.3) !important;
        border-color: #6366F1 !important;
        color: #F1F5F9 !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-header">
    <div class="hero-title">🏢 Smart Colombo Apartment Finder</div>
    <div class="hero-subtitle">✨ Find Your Dream Home in Minutes with AI-Powered Recommendations</div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.2)); border-radius: 20px; margin-bottom: 2rem; border: 1px solid rgba(99, 102, 241, 0.3);'>
        <h2 style='color: #F1F5F9; margin: 0;'>💰 Price Guide</h2>
        <p style='color: #94A3B8; margin-top: 0.5rem; font-size: 0.9rem;'>Colombo Real Estate Market</p>
    </div>
    """, unsafe_allow_html=True)
    
    price_data = [
        ("💰", "Low", "Under Rs. 2 Crores", "#10B981"),
        ("💸", "Low-Medium", "Rs. 2-4 Crores", "#14B8A6"),
        ("🏠", "Medium", "Rs. 4-6 Crores", "#6366F1"),
        ("⭐", "Medium-High", "Rs. 6-8 Crores", "#8B5CF6"),
        ("✨", "High", "Rs. 8-10 Crores", "#D946EF"),
        ("👑", "Premium", "Over Rs. 10 Crores", "#F59E0B")
    ]
    
    for icon, range_name, range_desc, color in price_data:
        st.markdown(f"""
        <div class='info-card' style='padding: 1rem; margin: 0.5rem 0; border-left-color: {color};'>
            <div style='display: flex; align-items: center; gap: 1rem;'>
                <span style='font-size: 1.8rem;'>{icon}</span>
                <div>
                    <strong style='color: #F1F5F9; font-size: 1.1rem;'>{range_name}</strong><br>
                    <span style='color: #94A3B8; font-size: 0.9rem;'>{range_desc}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem; background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.2)); border-radius: 20px; margin: 1rem 0; border: 1px solid rgba(16, 185, 129, 0.3);'>
        <h3 style='color: #F1F5F9; margin: 0;'>📍 Popular Areas</h3>
        <p style='color: #94A3B8; margin-top: 0.5rem; font-size: 0.9rem;'>Premium Locations in Colombo</p>
    </div>
    """, unsafe_allow_html=True)
    
    areas = [
        ("🏛️", "Colombo 1", "Fort - Commercial Hub"),
        ("🌆", "Colombo 2", "Slave Island - Mixed Use"),
        ("💎", "Colombo 3", "Kollupitiya - Premium"),
        ("🌊", "Colombo 4", "Bambalapitiya - Beachside"),
        ("🏡", "Colombo 5", "Havelock - Residential"),
        ("💰", "Colombo 6", "Wellawatte - Affordable"),
        ("🏰", "Colombo 7", "Cinnamon Gardens - Luxury")
    ]
    
    for icon, area, desc in areas:
        st.markdown(f"""
        <div class='area-badge'>
            <span style='font-size: 1.2rem; margin-right: 0.5rem;'>{icon}</span>
            <strong style='color: #F1F5F9;'>{area}</strong>
            <br>
            <span style='color: #94A3B8; font-size: 0.85rem; margin-left: 1.8rem;'>{desc}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4 style='color: #F1F5F9; margin-bottom: 1rem;'>📊 Quick Stats</h4>
        <div style='color: #94A3B8;'>
            <div style='margin: 0.5rem 0;'>🏢 <strong>15+</strong> Apartments Available</div>
            <div style='margin: 0.5rem 0;'>⭐ <strong>4.5+</strong> Average Rating</div>
            <div style='margin: 0.5rem 0;'>🎯 <strong>AI-Powered</strong> Matching</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

questions = [
    {
        "question": "Which area in Colombo interests you?", 
        "icon": "📍",
        "placeholder": "e.g., Colombo 3, Colombo 7, or 'any'",
        "hint": "Choose from Colombo 1-7 or type 'any' for all areas",
        "examples": ["Colombo 3", "Colombo 7", "Any"]
    },
    {
        "question": "Do you have a preferred developer?", 
        "icon": "🏗️",
        "placeholder": "e.g., Altair Group, Overseas Realty, or 'any'",
        "hint": "Specify a trusted developer or type 'any'",
        "examples": ["Altair Group", "Overseas Realty", "Any"]
    },
    {
        "question": "What amenities matter most to you?", 
        "icon": "🏊",
        "placeholder": "e.g., swimming pool, gym, parking, security",
        "hint": "Separate multiple amenities with commas",
        "examples": ["swimming pool, gym", "parking, security", "Any"]
    },
    {
        "question": "What's your preferred price range?", 
        "icon": "💰",
        "placeholder": "Low, Medium, High, Premium, or 'any'",
        "hint": "Choose from: Low, Low-Medium, Medium, Medium-High, High, Premium",
        "examples": ["Medium", "High", "Premium", "Any"]
    },
    {
        "question": "What type of apartment suits you best?", 
        "icon": "🎯",
        "placeholder": "e.g., Luxury, Standard, Eco-Friendly, or 'any'",
        "hint": "Describe your ideal apartment style",
        "examples": ["Luxury", "Standard", "Penthouse", "Any"]
    },
    {
        "question": "How many bedrooms do you need?", 
        "icon": "🛏️",
        "placeholder": "e.g., 1, 2, 3, 4, or 'any'",
        "hint": "Enter a number or 'any' for flexible options",
        "examples": ["2", "3", "Any"]
    },
    {
        "question": "How many bathrooms would you like?", 
        "icon": "🚿",
        "placeholder": "e.g., 1, 2, 3, or 'any'",
        "hint": "Enter a number or 'any'",
        "examples": ["2", "3", "Any"]
    },
    {
        "question": "What floor number do you prefer? (Higher floors = better views, Lower floors = easier access)", 
        "icon": "🏢",
        "placeholder": "e.g., 5, 10, 15, or 'any'",
        "hint": "Enter your preferred floor number. Higher floors have better views, lower floors are more accessible.",
        "examples": ["5", "10", "Any"]
    },
    {
        "question": "What's your minimum acceptable rating?", 
        "icon": "⭐",
        "placeholder": "e.g., 4.0, 4.5, or leave blank",
        "hint": "Rate from 1.0 to 5.0, or leave empty for any rating",
        "examples": ["4.0", "4.5", "Any"]
    },
]

keys_order = ["location", "developer", "amenities", "price_range", "apartment_type", "bedrooms", "bathrooms", "floor_number", "rating"]

if "user_params" not in st.session_state:
    st.session_state.user_params = {
        "location": None,
        "developer": None,
        "amenities": set(),
        "price_range": None,
        "apartment_type": None,
        "bedrooms": None,
        "bathrooms": None,
        "floor_number": 0,
        "rating": None,
    }

if "step" not in st.session_state:
    st.session_state.step = 0

if "messages" not in st.session_state:
    st.session_state["messages"] = [{
        "role": "assistant", 
        "content": "👋 Welcome to your AI-powered apartment advisor! I'll ask you 9 quick questions to find your perfect home in Colombo. Let's get started! 🚀"
    }]

col_left, col_center, col_right = st.columns([1, 6, 1])

with col_center:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if st.session_state.step < len(questions):
        current_question = questions[st.session_state.step]
        
        st.markdown(f"""
        <div class='question-card'>
            <div class='question-number'>Question {st.session_state.step + 1}/{len(questions)}</div>
            <div class='question-text'>{current_question['icon']} {current_question['question']}</div>
            <div class='question-hint'>💡 {current_question['hint']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin: 1rem 0;'>", unsafe_allow_html=True)
        cols = st.columns(len(current_question['examples']))
        for idx, example in enumerate(current_question['examples']):
            with cols[idx]:
                if st.button(f" {example}", key=f"quick_{st.session_state.step}_{idx}", use_container_width=True):
                    user_input = example
                    key = keys_order[st.session_state.step]
                    
                    if key == "amenities":
                        st.session_state.user_params[key] = set([x.strip() for x in user_input.split(",")]) if user_input.lower() != "any" else set()
                    elif key in ["bedrooms", "bathrooms", "floor_number"]:
                        try:
                            if user_input.lower() in ["any", "no preference", ""]:
                                st.session_state.user_params[key] = 0
                            else:
                                st.session_state.user_params[key] = int(user_input)
                        except ValueError:
                            st.session_state.user_params[key] = 0
                    elif key == "rating":
                        try:
                            if user_input.lower() in ["any", "no preference", ""]:
                                st.session_state.user_params[key] = None
                            else:
                                st.session_state.user_params[key] = float(user_input)
                        except ValueError:
                            st.session_state.user_params[key] = None
                    else:
                        st.session_state.user_params[key] = user_input.strip() if user_input and user_input.lower() not in ["any", "no preference"] else None

                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.step += 1
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center; color: #64748B; margin: 1rem 0; font-size: 0.9rem;'>or enter your custom answer below:</div>", unsafe_allow_html=True)
        
        user_input = st.text_input(
            "Your answer:",
            placeholder=current_question["placeholder"],
            key=f"input_text_{st.session_state.step}",
            label_visibility="collapsed"
        )
        
        col_btn1, col_btn2, col_btn3 = st.columns([2, 3, 2])
        
        with col_btn1:
            if st.button("⏭️ Skip", key=f"skip_{st.session_state.step}", use_container_width=True):
                key = keys_order[st.session_state.step]
                st.session_state.user_params[key] = None if key != "floor_number" else 0
                st.session_state.messages.append({"role": "user", "content": "Skipped"})
                st.session_state.step += 1
                st.rerun()
        
        with col_btn2:
            if st.button("🚀 Continue", key=f"btn_{st.session_state.step}", use_container_width=True):
                if user_input.strip():
                    key = keys_order[st.session_state.step]
                    
                    if key == "amenities":
                        st.session_state.user_params[key] = set([x.strip() for x in user_input.split(",")]) if user_input else set()
                    elif key in ["bedrooms", "bathrooms", "floor_number"]:
                        try:
                            if user_input.lower() in ["any", "no preference", ""]:
                                st.session_state.user_params[key] = 0
                            else:
                                st.session_state.user_params[key] = int(user_input)
                        except ValueError:
                            st.error("⚠️ Please enter a valid number or 'any'.")
                            st.stop()
                    elif key == "rating":
                        try:
                            if user_input.lower() in ["any", "no preference", ""]:
                                st.session_state.user_params[key] = None
                            else:
                                st.session_state.user_params[key] = float(user_input)
                        except ValueError:
                            st.error("⚠️ Please enter a valid rating (e.g., 4.5) or 'any'.")
                            st.stop()
                    else:
                        st.session_state.user_params[key] = user_input.strip() if user_input and user_input.lower() not in ["any", "no preference"] else None

                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.step += 1
                    st.rerun()
                else:
                    st.warning("⚠️ Please provide an answer or click Skip to continue.")
        
        with col_btn3:
            if st.button("🔄 Reset", key=f"reset_{st.session_state.step}", use_container_width=True):
                st.session_state.step = 0
                st.session_state.user_params = {
                    "location": None,
                    "developer": None,
                    "amenities": set(),
                    "price_range": None,
                    "apartment_type": None,
                    "bedrooms": None,
                    "bathrooms": None,
                    "floor_number": 0,
                    "rating": None,
                }
                st.session_state.messages = [{
                    "role": "assistant", 
                    "content": "👋 Welcome back! Let's start fresh and find your perfect apartment! 🚀"
                }]
                response.clear()
                st.rerun()

    if st.session_state.step == len(questions):
        st.markdown("""
        <div class='success-icon' style='text-align: center; margin: 2rem 0;'>
            <div style='font-size: 5rem;'>🎉</div>
            <h2 style='color: #10B981; margin-top: 1rem;'>All Set!</h2>
            <p style='color: #94A3B8; font-size: 1.1rem;'>Finding your perfect matches...</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📋 Your Preferences Summary", expanded=True):
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.9)); padding: 2rem; border-radius: 20px; border: 1px solid rgba(99, 102, 241, 0.3);'>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #6366F1;'>📍 Location:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{st.session_state.user_params["location"] or "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #6366F1;'>🏗️ Developer:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{st.session_state.user_params["developer"] or "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #6366F1;'>💰 Price Range:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{st.session_state.user_params["price_range"] or "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #6366F1;'>🎯 Type:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{st.session_state.user_params["apartment_type"] or "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #10B981;'>🛏️ Bedrooms:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{str(st.session_state.user_params["bedrooms"]) if st.session_state.user_params["bedrooms"] else "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #10B981;'>🚿 Bathrooms:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{str(st.session_state.user_params["bathrooms"]) if st.session_state.user_params["bathrooms"] else "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #10B981;'>🏢 Min Floor:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{str(st.session_state.user_params["floor_number"]) if st.session_state.user_params["floor_number"] is not None and st.session_state.user_params["floor_number"] != 0 else "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #10B981;'>⭐ Min Rating:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{str(st.session_state.user_params["rating"]) if st.session_state.user_params["rating"] else "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class='info-card' style='margin: 0.5rem 0;'>
                    <strong style='color: #10B981;'>🏊 Amenities:</strong>
                    <div style='color: #F1F5F9; font-size: 1.1rem; margin-top: 0.3rem;'>{", ".join(st.session_state.user_params["amenities"]) if st.session_state.user_params["amenities"] else "Any"}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

        user_params_fact = ApartmentFact(
            location=st.session_state.user_params["location"] or "",
            developer=st.session_state.user_params["developer"] or "",
            amenities=st.session_state.user_params["amenities"] or set(),
            price_range=st.session_state.user_params["price_range"] or "",
            apartment_type=st.session_state.user_params["apartment_type"] or "",
            bedrooms=st.session_state.user_params["bedrooms"] or 0,
            bathrooms=st.session_state.user_params["bathrooms"] or 0,
            rating=st.session_state.user_params["rating"] or 0,
            floor_number=st.session_state.user_params["floor_number"] or 0,
            price=0,
            area_sqft=0,
            completion_year=0
        )

        with st.spinner("🔍 Analyzing 15+ premium apartments in Colombo..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            engine = ApartmentAdvisorSystem(knowledge_base)
            engine.reset()
            engine.declare(user_params_fact)
            engine.run()
            
            progress_bar.empty()

        st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align: center; margin: 3rem 0;'>
            <h1 style='font-size: 3rem; background: linear-gradient(135deg, #6366F1, #8B5CF6, #10B981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900;'>
                🎯 Your Personalized Matches
            </h1>
            <p style='color: #94A3B8; font-size: 1.2rem; margin-top: 1rem;'>Handpicked apartments just for you</p>
        </div>
        """, unsafe_allow_html=True)
        
        if response.get("response_message"):
            st.markdown(f"""
            <div class='info-box' style='text-align: center; padding: 2rem;'>
                <h3 style='color: #F1F5F9; margin: 0;'>{response["response_message"]}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        if response.get("response_data"):
            for i, apartment_data in enumerate(response["response_data"], start=1):
                if isinstance(apartment_data, tuple) and len(apartment_data) == 3:
                    apartment, score, explanation = apartment_data
                    
                    st.markdown(f"""
                    <div class='apartment-card'>
                        <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1.5rem;'>
                            <div>
                                <h2 style='color: #F1F5F9; margin: 0; font-size: 1.8rem;'>🏢 {apartment.get('title', 'Unknown Title')}</h2>
                            </div>
                            <div class='match-score'>🎯 {score}% Match</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns([2, 2, 2])
                    
                    with col1:
                        st.markdown(f"""
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>📍 Location</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('location', 'Unknown')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🏗️ Developer</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('developer', 'Unknown')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>💰 Price</span><br>
                            <div class='price-highlight'>{format_price(apartment.get('price', 0))}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🎯 Type</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('apartment_type', 'N/A')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🛏️ Bedrooms</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('bedrooms', 'N/A')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🚿 Bathrooms</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('bathrooms', 'N/A')}</strong>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(f"""
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>📐 Area</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('area_sqft', 'N/A'):,} sqft</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🏢 Floor</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('floor_number', 'N/A')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>⭐ Rating</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('rating', 'N/A')}/5.0</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>📅 Completed</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('completion_year', 'N/A')}</strong>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
                    
                    amenities_list = apartment.get('amenities', [])
                    if amenities_list:
                        st.markdown("<span style='color: #94A3B8;'>🏊 Amenities:</span>", unsafe_allow_html=True)
                        amenities_html = " ".join([f"<span class='badge badge-primary'>{amenity}</span>" for amenity in amenities_list])
                        st.markdown(f"<div style='margin-top: 0.5rem;'>{amenities_html}</div>", unsafe_allow_html=True)
                    
                    if explanation:
                        st.markdown(f"""
                        <div style='margin-top: 1.5rem; padding: 1.2rem; background: rgba(16, 185, 129, 0.1); border-radius: 15px; border-left: 4px solid #10B981;'>
                            <strong style='color: #10B981;'>🤔 Why this match:</strong><br>
                            <span style='color: #F1F5F9; margin-top: 0.5rem; display: block;'>{explanation}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                elif isinstance(apartment_data, dict):
                    apartment = apartment_data
                    
                    st.markdown(f"""
                    <div class='apartment-card'>
                        <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1.5rem;'>
                            <div>
                                <h2 style='color: #F1F5F9; margin: 0; font-size: 1.8rem;'>🏢 {apartment.get('title', 'Unknown Title')}</h2>
                            </div>
                            <div class='match-score'> Perfect Match</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns([2, 2, 2])
                    
                    with col1:
                        st.markdown(f"""
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>📍 Location</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('location', 'Unknown')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🏗️ Developer</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('developer', 'Unknown')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>💰 Price</span><br>
                            <div class='price-highlight'>{format_price(apartment.get('price', 0))}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🎯 Type</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('apartment_type', 'N/A')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🛏️ Bedrooms</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('bedrooms', 'N/A')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🚿 Bathrooms</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('bathrooms', 'N/A')}</strong>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(f"""
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>📐 Area</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('area_sqft', 'N/A'):,} sqft</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>🏢 Floor</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('floor_number', 'N/A')}</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>⭐ Rating</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('rating', 'N/A')}/5.0</strong>
                        </div>
                        <div style='margin: 0.8rem 0;'>
                            <span style='color: #94A3B8;'>📅 Completed</span><br>
                            <strong style='color: #F1F5F9; font-size: 1.1rem;'>{apartment.get('completion_year', 'N/A')}</strong>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
                    
                    amenities_list = apartment.get('amenities', [])
                    if amenities_list:
                        st.markdown("<span style='color: #94A3B8;'>🏊 Amenities:</span>", unsafe_allow_html=True)
                        amenities_html = " ".join([f"<span class='badge badge-success'>{amenity}</span>" for amenity in amenities_list])
                        st.markdown(f"<div style='margin-top: 0.5rem;'>{amenities_html}</div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
        
        else:
            st.markdown("""
            <div class='info-box' style='text-align: center; padding: 3rem;'>
                <div style='font-size: 4rem; margin-bottom: 1rem;'>😔</div>
                <h3 style='color: #F1F5F9;'>No matches found</h3>
                <p style='color: #94A3B8; margin-top: 1rem;'>Try adjusting your preferences for better results</p>
            </div>
            """, unsafe_allow_html=True)
        
        if response.get("explanations"):
            with st.expander("🤔 How We Made These Recommendations", expanded=False):
                st.markdown("""
                <div style='background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.9)); padding: 1.5rem; border-radius: 15px;'>
                """, unsafe_allow_html=True)
                
                for explanation in response["explanations"]:
                    st.markdown(f"""
                    <div style='background: rgba(51, 65, 85, 0.6); padding: 1.2rem; border-radius: 12px; margin: 0.8rem 0; border-left: 4px solid #10B981;'>
                        <strong style='color: #10B981; font-size: 1.1rem;'>🏢 {explanation['apartment']}</strong><br>
                        <span style='color: #F1F5F9; margin-top: 0.5rem; display: block;'>{explanation['explanation']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Start New Search", use_container_width=True, key="final_reset"):
                st.session_state.step = 0
                st.session_state.user_params = {
                    "location": None,
                    "developer": None,
                    "amenities": set(),
                    "price_range": None,
                    "apartment_type": None,
                    "bedrooms": None,
                    "bathrooms": None,
                    "floor_number": 0,
                    "rating": None,
                }
                st.session_state.messages = [{
                    "role": "assistant", 
                    "content": "👋 Welcome back! Ready to find another perfect home? Let's go! 🚀"
                }]
                response.clear()
                st.rerun()

st.markdown("""
<div style='text-align: center; padding: 3rem 1rem; margin-top: 4rem; border-top: 1px solid #334155;'>
    <p style='color: #64748B; font-size: 0.9rem;'>
        🏢 Powered by AI | Made with ❤️ for Colombo Real Estate
    </p>
    <p style='color: #475569; font-size: 0.8rem; margin-top: 0.5rem;'>
        © 2025 Smart Colombo Apartment Finder | All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)