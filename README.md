# 🏢 Colombo Apartment Advisor - Expert System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Experta](https://img.shields.io/badge/Experta-0.24.0-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red?style=for-the-badge&logo=streamlit)

**AI-Powered Apartment Recommendation System using Rule-Based Expert System**


</div>

## 📖 Overview

The Colombo Apartment Advisor is an intelligent rule-based expert system that helps users find their perfect apartment in Colombo, Sri Lanka. Built using the Experta rule engine and featuring a modern Streamlit interface, this system provides personalized apartment recommendations based on user preferences.

### 🎯 What Problem Does It Solve?

- **Information Overload**: 30+ premium apartments with varying features
- **Complex Decision Making**: Multiple criteria including location, price, amenities, floor preferences
- **Personalized Matching**: Finding apartments that truly match individual needs
- **Expert Knowledge**: Encapsulating real estate expertise in an accessible system


### 🧠 Intelligent Rule-Based System
- **Multi-criteria Matching** using Experta rule engine
- **Exact Match Detection** for perfect preference alignment
- **Smart Alternatives** with relevance scoring (40-100%)
- **Contextual Explanations** for each recommendation
- **Handles Incomplete Information** for each recommendation
- **Flexible Preference Handling** with "any" option support

## 🚀 Installation

### Prerequisites
* Python 3.8 or higher
* pip package manager

### Step-by-Step Setup

### 1. Clone or Download the Project
```bash
# Create project directory
mkdir colombo-apartment-expert-system
cd colombo-apartment-expert-system
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install experta streamlit
```

### 4. Project Structure
Place all Python files in the same directory:
* `controller.py`
* `facts.py`
* `main.py`
* `st.py`

## 🎯 Usage

### Starting the Application
```bash
streamlit run st.py
```

The application will open in your default browser at `http://localhost:8501`
