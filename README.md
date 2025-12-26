# F1-Telemetry
# Formula 1 Telemetry Analysis Dashboard

A full-stack web application built with **Flask**, **MySQL**, and **Python** to visualize and compare Formula 1 driver performance across multiple races. The system stores telemetry data such as lap times, speed, acceleration, throttle, and gear usage, allowing users to analyze race metrics through an interactive dashboard.

## Features
- Interactive dashboard for comparing driver telemetry data.
- RESTful APIs for races, drivers, and telemetry endpoints.
- MySQL database with normalized schema for races, drivers, and telemetry.
- Automated data generation for synthetic race and driver stats.
- Session-based authentication and user access control.

## Tech Stack
- **Backend:** Flask, Python, MySQL Connector  
- **Frontend:** HTML, CSS, JavaScript (AJAX)  
- **Database:** MySQL  
- **Data Simulation:** Python scripts to generate telemetry data

## How It Works
1. Initialize the database and create tables using `database.py`.
2. Populate sample data (races, drivers, telemetry) using `data.py`.
3. Run `app.py` or `dashboard.py` to start the Flask server.
4. Open the dashboard in your browser to compare telemetry stats for selected drivers.

This project demonstrates skills in full-stack development, SQL integration, REST API design, and analytical data visualization.
