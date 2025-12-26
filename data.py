from database import db_query
import random
from datetime import datetime

# Function to generate random telemetry data
def generate_telemetry_data(lap_number):
    return {
        "lap_time": round(random.uniform(75.0, 85.0), 3),  # Random lap time between 75.0 and 85.0 seconds
        "speed": round(random.uniform(300.0, 350.0), 1),   # Random speed between 300.0 and 350.0 km/h
        "acceleration": round(random.uniform(2.0, 3.0), 1), # Random acceleration between 2.0 and 3.0 m/s²
        "brake": round(random.uniform(1.0, 2.0), 1),       # Random brake force between 1.0 and 2.0
        "throttle": round(random.uniform(0.0, 1.0), 2),    # Throttle (0% to 100%)
        "gear": random.randint(1, 8)                      # Gear (1 to 8)
    }

# Insert sample races
def insert_races():
    races = [
        ("Monaco Grand Prix", datetime(2023, 5, 28)),
        ("Silverstone Grand Prix", datetime(2023, 7, 9)),
        ("Suzuka Grand Prix", datetime(2023, 10, 8)),
        ("Monza Grand Prix", datetime(2023, 9, 3)),
        ("Spa-Francorchamps Grand Prix", datetime(2023, 8, 27)),
        ("Interlagos Grand Prix", datetime(2023, 11, 12)),
        ("Melbourne Grand Prix", datetime(2023, 4, 2)),
        ("Montreal Grand Prix", datetime(2023, 6, 18)),
        ("Singapore Grand Prix", datetime(2023, 9, 17)),
        ("Abu Dhabi Grand Prix", datetime(2023, 11, 26))
    ]

    for race in races:
        db_query("""
            INSERT INTO races (race_name, race_date)
            VALUES (%s, %s)
        """, (race[0], race[1]), fetch=False)

    print("Inserted 10 races.")

# Insert sample drivers
def insert_drivers():
    drivers = [
        "Lewis Hamilton", "Max Verstappen", "Charles Leclerc", "Sergio Perez",
        "Carlos Sainz", "Lando Norris", "George Russell", "Fernando Alonso",
        "Esteban Ocon", "Pierre Gasly", "Valtteri Bottas", "Zhou Guanyu",
        "Kevin Magnussen", "Nico Hulkenberg", "Yuki Tsunoda", "Nyck de Vries",
        "Alex Albon", "Logan Sargeant", "Oscar Piastri", "Lance Stroll"
    ]

    for driver in drivers:
        db_query("""
            INSERT INTO drivers (driver_name)
            VALUES (%s)
        """, (driver,), fetch=False)

    print("Inserted 20 drivers.")

# Insert sample telemetry data for all races and drivers
def insert_telemetry():
    races = db_query("SELECT race_id FROM races")
    drivers = db_query("SELECT driver_id FROM drivers")

    for race in races:
        race_id = race[0]
        for driver in drivers:
            driver_id = driver[0]
            for lap_number in range(1, 11):  # 10 laps per driver per race
                telemetry = generate_telemetry_data(lap_number)
                db_query("""
                    INSERT INTO telemetry (race_id, driver_id, lap_number, lap_time, speed, acceleration, brake, throttle, gear)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (race_id, driver_id, lap_number, telemetry["lap_time"], telemetry["speed"], telemetry["acceleration"], telemetry["brake"], telemetry["throttle"], telemetry["gear"]), fetch=False)

    print("Inserted telemetry data for all races and drivers.")

# Main function to insert all data
def main():
    insert_races()
    insert_drivers()
    insert_telemetry()
    print("Data insertion complete.")

if __name__ == "__main__":
    main()