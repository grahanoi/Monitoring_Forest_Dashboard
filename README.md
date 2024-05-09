# PiPerformanceMonitor

## Raspberry Pi Performance Monitor
### Overview
This repository contains all the necessary components for setting up a performance monitoring system on a Raspberry Pi. It includes a Python script for collecting CPU temperature and utilization data, a Dockerfile for containerized deployment, and a Grafana dashboard for real-time visualization of the metrics.

### Features
CPU Temperature Monitoring: Measures the temperature of the Raspberry Pi's CPU in real-time.
CPU Utilization Tracking: Monitors the CPU usage to understand the load and performance.
Data Storage: Utilizes InfluxDB to store collected data efficiently.
Visualization: Features a Grafana dashboard to visualize the data through gauges and time series graphs.
### Components
monitor.py: Python script to collect CPU metrics and store them in InfluxDB.
Dockerfile: Contains all specifications to containerize the monitoring script.
dashboard.json: Grafana dashboard configuration file for importing and viewing collected data.
Setup Instructions
### Prerequisites
Docker installed on your Raspberry Pi
InfluxDB and Grafana setup on your Raspberry Pi or accessible remotely
