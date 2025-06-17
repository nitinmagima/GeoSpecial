import streamlit as st

# — App config —
st.set_page_config(
    page_title="UNICEF Cyclone Impact Explorer",
    page_icon="🌪️",
    layout="wide"
)

# — Title and Subtitle —
st.title("🌪️ UNICEF Cyclone Impact Explorer")
st.subheader("AI-powered insights to protect children before, during, and after a disaster")

# — Introduction —
st.markdown("""
Welcome to the UNICEF Cyclone Impact Explorer — a child-focused, AI-enabled platform for anticipatory disaster response in Bangladesh. This tool helps decision-makers understand risks, prioritize interventions, and act early to protect vulnerable populations.
""")

# — Key Features —
st.markdown("### 🔍 Platform Highlights")
st.markdown("""
- 🌀 **Historical Cyclone Analysis**: Visualize past cyclone tracks, recurrence patterns, and hotspots  
- ⏳ **Crisis Timeline**: Align forecast lead times with expected disruptions to health, education, and protection  
- 📈 **Scenario Modeling**: Use GEV and Monte Carlo simulations to forecast cyclone intensities and impacts  
- 🧒 **Exposure Mapping**: Estimate children exposed by age group and location using population rasters  
- 🏥 **Infrastructure Risks**: Evaluate schools, clinics, and water points at risk of storm impact  
- 🤖 **AI Action Assistant**: Ask questions and receive real-time action prompts from a GPT-powered chatbot  
- 📡 **Monitoring & Alerts**: Connect to live forecasts and display real-time risk alerts
""")

# — How to Use Each Page —
st.markdown("### 🧭 How to Navigate This App")
st.markdown("""
1. **Home**: Start here to understand the platform’s purpose and how to navigate it.

2. **1 - Defining Risk & Timeline**  
   Explore cyclone hazard zones, analyze exposure layers (admin boundaries, population), and align lead times with sector-specific risks.

3. **2 - Scenario Forecasting**  
   Use AI-powered models to simulate return periods and storm scenarios. Prioritize actions using forecast confidence bands and impact thresholds.

4. **3 - AI Chatbot for Action**  
   Interact with an AI assistant trained on UNICEF protocols. Ask what actions to take given a location or impact, and get tailored recommendations.

5. **4 - Monitoring & Alerts**  
   Visualize live data feeds and thresholds. Get auto-alerts when risk conditions are met and generate situation reports.

6. **5 - Exposure Dashboard**  
   Assess risk to critical infrastructure and population. View vulnerability hotspots and zoomable imagery (e.g. education facilities, clinics, flood zones).

7. **6 - Reference Tools & Reports**  
   Access real-time dashboards and external databases like UNOSAT, PreventionWeb, and IFRC with disaster publications and emergency maps.
""")

# — Data Sources —
st.markdown("### 📚 Data Sources")
st.markdown("""
- Cyclone track archives and probabilistic forecasts  
- Admin boundaries (GADM, OSM), child population grids  
- Infrastructure datasets from HOTOSM and UNICEF GIGA  
- Vulnerability indicators (malnutrition, vaccination, access)
""")

# — Support —
st.markdown("### 🛠️ Support")
st.markdown("For technical support, contact the development team.")

# — Visual Highlights —
col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Past Events**\n\nExplore historical cyclone paths to inform planning.")

with col2:
    st.warning("**Risk Timeline**\n\nForecast lead time vs. sector disruptions.")

with col3:
    st.success("**AI + Monitoring**\n\nAutomate alerts, actions, and situational awareness.")
