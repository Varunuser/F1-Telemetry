from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'f1_telemetry'
}

def db_query(query, params=None, fetch=True):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    if fetch:
        result = cursor.fetchall()
    else:
        conn.commit()
        result = None
    cursor.close()
    conn.close()
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_races')
def get_races():
    races = db_query("SELECT race_id, race_name FROM races")
    return jsonify(races)

@app.route('/get_drivers')
def get_drivers():
    drivers = db_query("SELECT driver_id, driver_name FROM drivers")
    return jsonify(drivers)

@app.route('/get_telemetry', methods=['POST'])
def get_telemetry():
    data = request.json
    race_id = data['race_id']
    driver1_id = data['driver1_id']
    driver2_id = data['driver2_id']

    telemetry1 = db_query("""
        SELECT lap_number, lap_time, speed, acceleration, brake 
        FROM telemetry 
        WHERE race_id = %s AND driver_id = %s
        ORDER BY lap_number
    """, (race_id, driver1_id))

    telemetry2 = db_query("""
        SELECT lap_number, lap_time, speed, acceleration, brake 
        FROM telemetry 
        WHERE race_id = %s AND driver_id = %s
        ORDER BY lap_number
    """, (race_id, driver2_id))

    return jsonify({
        'driver1': telemetry1,
        'driver2': telemetry2
    })

if __name__ == '__main__':
    app.run(debug=True)