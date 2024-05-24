# Monitoring_Forest_Dashboard

## Overview
This project focuses on quantifying, analyzing, and assessing the results of NDVI analysis conducted in Project Work II, which aimed to monitor the health of a forest over different seasons. The goal is to address the quality, reliability, and uncertainty of the results using a Streamlit dashboard.

## Project Structure
- **data/**: Contains GeoTIFF files representing seasonal and mean NDVI values.
- **scripts/**: Python scripts for data processing and visualization.
  - `visualization.py`: Script to generate visualizations from the processed data.
- **dashboard/**: Contains the Streamlit app for the interactive dashboard.
  - `dashboard.py`: Main script to run the Streamlit dashboard.
- **README.md**: Project documentation.
- **requirements.txt**: List of Python dependencies.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/Monitoring_Forest_Dashboard.git
    cd Monitoring_Forest_Dashboard
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    python                    3.12.3
    matplotlib                3.8.4
    streamlit                 1.32.0
    folium                    0.14.0
    streamlit-folium          0.20.0
    rasterio                  1.2.10
    pip install -r requirements.txt
    ```

## Running the Dashboard
To start the Streamlit dashboard, navigate to the `dashboard/` directory and run:
```sh
cd dashboard
streamlit run dashboard.py
