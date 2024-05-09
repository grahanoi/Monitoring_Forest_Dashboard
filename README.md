# PiPerformanceMonitor
Raspberry Pi Performance Monitor
Overview
This repository contains all the necessary components for setting up a performance monitoring system on a Raspberry Pi. It includes a Python script for collecting CPU temperature and utilization data, a Dockerfile for containerized deployment, and a Grafana dashboard for real-time visualization of the metrics.

Features
CPU Temperature Monitoring: Measures the temperature of the Raspberry Pi's CPU in real-time.
CPU Utilization Tracking: Monitors the CPU usage to understand the load and performance.
Data Storage: Utilizes InfluxDB to store collected data efficiently.
Visualization: Features a Grafana dashboard to visualize the data through gauges and time series graphs.
Components
monitor.py: Python script to collect CPU metrics and store them in InfluxDB.
Dockerfile: Contains all specifications to containerize the monitoring script.
dashboard.json: Grafana dashboard configuration file for importing and viewing collected data.
Setup Instructions
Prerequisites
Docker installed on your Raspberry Pi
InfluxDB and Grafana setup on your Raspberry Pi or accessible remotely
Installation
Clone the Repository:
bash
Copy code
git clone https://<your-git-server>/username/RaspberryPi_Monitoring.git
cd RaspberryPi_Monitoring
Build the Docker Image:
bash
Copy code
docker build -t raspberry_monitor .
Run the Docker Container:
bash
Copy code
docker run -d raspberry_monitor
Set up Grafana Dashboard:
Import the dashboard.json file into your Grafana instance to visualize the metrics.
Usage
Once the Docker container is running, it will automatically start collecting data every minute and store it in InfluxDB. You can view the metrics in real-time using the Grafana dashboard.

Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
