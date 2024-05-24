import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import folium
from streamlit_folium import st_folium
import rasterio
from rasterio.plot import show

# Title and description
st.title("Monitoring Forest Health Across Seasons with NDVI Analysis in GEE")
st.markdown("""
This project focuses on monitoring the health of a forest over the course of a year to identify seasonal variations in vegetation health using NDVI analysis. Utilizing remote sensing data provided by Sentinel-2 satellite imagery and processed in Google Earth Engine (GEE), we analyze and visualize dynamic changes in forest vegetation.
""")

# Objectives
st.header("Objectives")
st.markdown("""
- Track seasonal growth patterns and health of the forest by calculating NDVI.
- Determine the periods of highest and lowest vegetation health.
- Identify deviations that might indicate environmental stress or ecological disturbances.
""")

# Methodology
st.header("Methodology")
st.markdown("""
1. **Data Acquisition**: High-resolution Sentinel-2 imagery was accessed.
2. **Area of Interest Definition**: The geographic scope of the study was defined using a polygon that covers the targeted forest area near Wollishofen.
3. **Seasonal Data Processing**:
   - Data Filtering: Selected images with less than 20% cloud cover.
   - NDVI Calculation: Calculated NDVI for each image and aggregated the values for each season.
4. **Data Visualization**:
   - Visualized in Google Earth Engine (GEE).
   - Exported NDVI images as GeoTIFF files to Google Drive.
   - Enhanced visualization in QGIS and compiled detailed maps in Python.
""")

# Display NDVI Images
st.header("Seasonal NDVI Images")

# Function to display GeoTIFF images
def display_geotiff(file_path):
    with rasterio.open(file_path) as src:
        fig, ax = plt.subplots(figsize=(10, 10))
        show(src, ax=ax)
        plt.title(f"NDVI Image: {file_path}")
        st.pyplot(fig)

# Display images for each season
seasons = ["Spring", "Summer", "Autumn", "Winter"]
for season in seasons:
    st.subheader(f"{season} NDVI")
    # Assuming you have the GeoTIFF files named accordingly
    geotiff_path = f"data/{season.lower()}_ndvi.tif"
    display_geotiff(geotiff_path)

# Folium map for NDVI visualization
st.header("Interactive Map")
map_center = [47.3477, 8.5521]  # Example coordinates for Wollishofen
m = folium.Map(location=map_center, zoom_start=12)
st_folium(m, width=700, height=500)

# Results
st.header("Results")
st.markdown("""
Utilizing Sentinel-2 imagery, seasonal variations in forest health near Wollishofen were monitored through NDVI analysis. The methodological approach ensured data quality by filtering images and aggregating NDVI values for each season. Visualization in Google Earth Engine and enhancements in QGIS facilitated interpretation, highlighting distinct seasonal patterns in vegetation health.
""")

# Interpretation and Further Work
st.header("Interpretation & Further Work")
st.markdown("""
NDVI analysis delineated distinct seasonal vegetation patterns: spring's gradual growth, summer's peak health, autumn's senescence, and winter's dormancy. Additionally, consistent red patterns throughout the year suggest non-vegetative areas such as soil or buildings. Identified deviations from expected patterns hint at potential stress periods or ecological disturbances, warranting further investigation into their causes. This holistic approach yields valuable insights for targeted interventions and long-term assessment of forest ecosystem dynamics.
""")

st.markdown("""
Exploring mean NDVI trends over an extended timeframe would offer additional insight into ecosystem development.
""")

# Load and display images
st.header("Seasonal NDVI and Mean NDVI Images")
image_spring = mpimg.imread('data/images/median_ndvi_spring.jpg')
image_summer = mpimg.imread('data/images/median_ndvi_summer.jpg')
image_autumn = mpimg.imread('data/images/median_ndvi_autum.jpg')
image_winter = mpimg.imread('data/images/median_ndvi_winter.jpg')
image_mean = mpimg.imread('data/images/mean2023.jpg')

st.image(image_spring, caption='Median NDVI Spring 2023', use_column_width=True)
st.image(image_summer, caption='Median NDVI Summer 2023', use_column_width=True)
st.image(image_autumn, caption='Median NDVI Autumn 2023', use_column_width=True)
st.image(image_winter, caption='Median NDVI Winter 2023', use_column_width=True)
st.image(image_mean, caption='Mean NDVI 2023', use_column_width=True)
