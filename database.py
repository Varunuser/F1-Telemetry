import mysql.connector as sql

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'root',  # Replace with your MySQL password
    'database': 'f1_telemetry'
}

# Function to execute database queries
def db_query(query, params=None, fetch=True):
    try:
        # Connect to the database
        mydb = sql.connect(**db_config)
        cursor = mydb.cursor()

        # Execute the query
        cursor.execute(query, params or ())

        # Fetch results if required
        if fetch:
            result = cursor.fetchall()
        else:
            mydb.commit()
            result = None

        # Close the cursor and connection
        cursor.close()
        mydb.close()

        return result

    except sql.Error as err:
        print(f"Database error: {err}")
        return None

# Initialize the database and create tables
def initialize_database():
    try:
        # Connect to MySQL server (without specifying a database)
        mydb = sql.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = mydb.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS f1_telemetry")

        # Close the connection
        cursor.close()
        mydb.close()

        # Reconnect to the newly created database
        mydb = sql.connect(**db_config)
        cursor = mydb.cursor()

        # Create races table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS races (
                race_id INT AUTO_INCREMENT PRIMARY KEY,
                race_name VARCHAR(255) NOT NULL,
                race_date DATE NOT NULL
            )
        """)

        # Create drivers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                driver_id INT AUTO_INCREMENT PRIMARY KEY,
                driver_name VARCHAR(255) NOT NULL
            )
        """)

        # Create telemetry table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS telemetry (
                telemetry_id INT AUTO_INCREMENT PRIMARY KEY,
                race_id INT,
                driver_id INT,
                lap_number INT,
                lap_time FLOAT,
                speed FLOAT,
                acceleration FLOAT,
                brake FLOAT,
                throttle FLOAT,
                gear INT,
                FOREIGN KEY (race_id) REFERENCES races(race_id) ON DELETE CASCADE,
                FOREIGN KEY (driver_id) REFERENCES drivers(driver_id) ON DELETE CASCADE
            )
        """)

        # Commit changes and close connection
        mydb.commit()
        cursor.close()
        mydb.close()

        print("Database and tables created successfully.")

    except sql.Error as err:
        print(f"Error initializing database: {err}")

# Initialize the database when this script is run
if __name__ == "__main__":
    initialize_database()