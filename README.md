# 🌪UNICEF Cyclone Impact Explorer

A child-centered, AI-powered geospatial decision-support platform to help UNICEF and the Government of Bangladesh shift from reactive response to anticipatory action in the face of tropical cyclones and extreme weather.

![App Screenshot](https://geospecial.streamlit.app/)

## Overview

This application allows users to:
- Analyze **historical cyclone tracks**
- Model **forward-looking scenarios** using Generalized Extreme Value (GEV) modeling
- Assess **infrastructure and population exposure**
- Explore **AI-driven vulnerability hotspots**
- Align sectoral risks across time using a **crisis timeline**
- Interact with an **AI chatbot assistant** for response planning
- Monitor live **alerts and forecasts**

Every second counts during a disaster — this platform helps decision-makers act early, communicate efficiently, and prioritize children in high-risk zones.

---

## Key Pages

| Page                         | Description |
|-----------------------------|-------------|
| **Home**                    | Overview and how-to |
| **Defining Risk**           | Load admin boundaries and visualize historical cyclone tracks |
| **Scenario Analysis**       | Fit GEV models and run Monte Carlo simulations for future risks |
| **Exposure Analysis**       | View schools, health facilities, and child population rasters |
| **Crisis Timeline**         | Align forecast timelines with sectoral impact lead times |
| **AI Assistant**            | Get response actions based on spatial context and UNICEF SOPs |
| **Monitoring & Alerts**     | Live forecast monitoring and trigger thresholds |

---

## Tech Stack

- **Frontend**: Streamlit, Streamlit-Folium, Pydeck, Plotly, Altair
- **Backend**: Python 3.10, Pandas, NumPy, GeoPandas
- **Geospatial**: Fiona, Rasterio, Shapefiles & GeoJSONs
- **AI Integration**: OpenAI GPT (via API)
- **Data Sources**: Cyclone tracks, child population rasters, school/clinic points, vulnerability indicators

---

## Installation

Clone this repo and install dependencies:

```bash
git clone https://github.com/nitinmagima/GeoSpecial.git
cd GeoSpecial
pip install -r requirements.txt
streamlit run Home.py
