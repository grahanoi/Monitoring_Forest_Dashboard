import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import folium
from streamlit_folium import st_folium
import pandas as pd
import seaborn as sns
import numpy as np
import ast
import os

# Set the base directory
base_dir = os.path.dirname(__file__)

# Load the CSV files using relative paths
mean_ndvi_df = pd.read_csv(os.path.join(base_dir, 'data', 'csv', 'mean_ndvi_2023.csv'))
spring_ndvi_df = pd.read_csv(os.path.join(base_dir, 'data', 'csv','Median_NDVI_Spring_2023.csv'))
summer_ndvi_df = pd.read_csv(os.path.join(base_dir, 'data','csv', 'Median_NDVI_Summer_2023.csv'))
autumn_ndvi_df = pd.read_csv(os.path.join(base_dir, 'data', 'csv','Median_NDVI_Autumn_2023.csv'))
winter_ndvi_df = pd.read_csv(os.path.join(base_dir, 'data','csv', 'Median_NDVI_Winter_2023.csv'))

# Function to convert string representations of lists to numeric values
def convert_ndvi_column(df):
    df['NDVI'] = df['NDVI'].apply(lambda x: np.mean(ast.literal_eval(x)))
    return df

# Apply the conversion to all DataFrames
mean_ndvi_df = convert_ndvi_column(mean_ndvi_df)
spring_ndvi_df = convert_ndvi_column(spring_ndvi_df)
summer_ndvi_df = convert_ndvi_column(summer_ndvi_df)
autumn_ndvi_df = convert_ndvi_column(autumn_ndvi_df)
winter_ndvi_df = convert_ndvi_column(winter_ndvi_df)

# Calculate statistics
def calculate_statistics(df):
    mean = df['NDVI'].mean()
    median = df['NDVI'].median()
    return mean, median

mean_stats = calculate_statistics(mean_ndvi_df)
spring_stats = calculate_statistics(spring_ndvi_df)
summer_stats = calculate_statistics(summer_ndvi_df)
autumn_stats = calculate_statistics(autumn_ndvi_df)
winter_stats = calculate_statistics(winter_ndvi_df)

# Create a DataFrame to display statistics
stats_df = pd.DataFrame({
    'Season': ['Yearly Mean', 'Spring', 'Summer', 'Autumn', 'Winter'],
    'Mean NDVI': [mean_stats[0], spring_stats[0], summer_stats[0], autumn_stats[0], winter_stats[0]],
    'Median NDVI': [mean_stats[1], spring_stats[1], summer_stats[1], autumn_stats[1], winter_stats[1]]
})


# Title and introduction
st.title("🌳 Forest Health Monitoring")
st.markdown("## 🗣 Play me: ⬇")
# Embed the audio recording
st.audio(os.path.join(base_dir, 'data', 'audio', 'INtroduction.pdf_pages_1_to_1.mp3'))
st.markdown("### 🌱 Seasonal NDVI analysis of forest health in Wollishofen using Sentinel-2 satellite imagery.")
# Insert the GIF
st.image(os.path.join(base_dir, 'data', 'images', 'Sentinel-2_composites.png'), caption='Sentinel-2 Satellite')
st.markdown("""🌐https://learn.opengeoedu.de/fernerkundung/vorlesung/copernicus/Sentinel-2-Teil-1""")
# Add NDVI definition
st.markdown("""
**What is NDVI?**
The Normalized Difference Vegetation Index (NDVI) is a numerical indicator that uses the visible and near-infrared bands of the electromagnetic spectrum to analyze remote sensing measurements and assess whether the target being observed contains live green vegetation or not.

**Why is NDVI Important?**
- **Monitoring Vegetation Health**: NDVI helps in monitoring the health and vigor of vegetation, essential for agriculture and forestry.
- **Drought Assessment**: It assists in identifying drought-affected areas, aiding in drought management and mitigation efforts.
- **Land Cover Classification**: NDVI is used in classifying land cover types, distinguishing between vegetation, water bodies, and bare soil.
""")
# Folium map for NDVI visualization
st.header("🌍 Interactive Map")
st.audio(os.path.join(base_dir, 'data', 'audio', 'interatice_map.pdf_pages_1_to_1.mp3'))
map_center = [47.330, 8.520]  # Center coordinates for Wollishofen
m = folium.Map(location=map_center, zoom_start=15)

# Define the area of interest using the provided coordinates
area_of_interest = folium.Polygon(
    locations=[
        [47.32384525534488, 8.518398621179392],
        [47.33728327695866, 8.518398621179392],
        [47.33728327695866, 8.52492175350361],
        [47.32384525534488, 8.52492175350361]
    ],
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity=0.2,
    popup='Area of Interest'
)
area_of_interest.add_to(m)

st_folium(m, width=700, height=500)

# Objectives
st.header("🎯 Objectives")
st.markdown("""
- Track forest health by calculating NDVI.
- Identify the best and worst seasons for vegetation health.
- Detect potential environmental stresses.
""")

# Methodology
st.header("🔬 Methodology")
st.markdown("""
1. **Data Acquisition**: Accessed Sentinel-2 imagery.
2. **AOI Definition**: Defined study area near Wollishofen.
3. **Processing**:
   - Filtered images with < 20% cloud cover.
   - Calculated and aggregated seasonal NDVI.
4. **Visualization**: Used GEE, QGIS, and Python.
""")
# Load and display processed images
st.header("🖼️ Processed Images")
st.audio(os.path.join(base_dir, 'data', 'audio', 'processed_images.pdf_pages_1_to_1.mp3'))
image_paths = [
    os.path.join(base_dir, 'data', 'images', 'mean2023.jpg'),
    os.path.join(base_dir, 'data', 'images', 'median_ndvi_spring.jpg'),
    os.path.join(base_dir, 'data', 'images', 'median_ndvi_summer.jpg'),
    os.path.join(base_dir, 'data', 'images', 'median_ndvi_autum.jpg'),
    os.path.join(base_dir, 'data', 'images', 'median_ndvi_winter.jpg')
]

# Titles for the images
titles = ["Mean", "Spring", "Summer", "Autumn", "Winter"]

# Display processed images
fig_processed, axs = plt.subplots(1, len(image_paths), figsize=(25, 15))
for ax, img_path, title in zip(axs, image_paths, titles):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.set_title(title)

st.pyplot(fig_processed)

# Display the NDVI statistics
st.header("📊 NDVI Statistics")
st.audio(os.path.join(base_dir, 'data', 'audio', 'statistics.pdf_pages_1_to_1.mp3'))
# Mean NDVI by Season
st.subheader("Mean NDVI value by Season")
fig_mean = plt.figure(figsize=(10, 6))
colors = ['#808080', '#ff9900', '#77dd77', '#ff9900', '#ff6961']  
sns.barplot(x='Season', y='Mean NDVI', data=stats_df, palette=colors)
plt.title('Mean NDVI by Season')
st.pyplot(fig_mean)

# Median NDVI by Season
st.subheader("Median NDVI value by Season")
fig_median = plt.figure(figsize=(10, 6))
sns.barplot(x='Season', y='Median NDVI', data=stats_df, palette=colors)
plt.title('Median NDVI by Season')
st.pyplot(fig_median)

# Analysis and Insights
st.header("Summary and Thanks 🌳🌞🍂❄️")
st.audio(os.path.join(base_dir, 'data', 'audio', 'end.pdf_pages_1_to_1.mp3'))

st.markdown("""
### Key Findings:
- **Summer** shows the highest mean NDVI, indicating peak vegetation health.🌞
- **Winter** has the lowest mean NDVI, reflecting dormancy or minimal vegetation.❄️
- **Spring and Autumn** transition periods show moderate NDVI values.🍃🍂
### Insights:
- The high NDVI in summer aligns with expected vigorous growth.🌿
- Low NDVI in winter suggests typical dormancy or leaf-off conditions.💤
- Identified deviations can indicate areas of concern requiring further investigation.🚨
            
### Author: [Noirin Graham](https://github.com/grahanoi)
### Author: [Felix Pascal](https://github.zhaw.com/felixpas)
""")

