from flask import Flask, render_template, request, jsonify, session, redirect
from database import db_query  # Import the database query function

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management

# ------------------------------ HOME ROUTE ------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# ------------------------------ DASHBOARD ROUTE ------------------------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')  # Redirect to login if user is not logged in

    return render_template('dashboard.html')

# ------------------------------ GET RACES ROUTE ------------------------------
@app.route('/get_races')
def get_races():
    races = db_query("SELECT race_id, race_name FROM races")
    if races:
        return jsonify(races)
    else:
        return jsonify({"status": "error", "message": "No races found"})

# ------------------------------ GET DRIVERS ROUTE ------------------------------
@app.route('/get_drivers')
def get_drivers():
    drivers = db_query("SELECT driver_id, driver_name FROM drivers")
    if drivers:
        return jsonify(drivers)
    else:
        return jsonify({"status": "error", "message": "No drivers found"})

# ------------------------------ GET TELEMETRY ROUTE ------------------------------
@app.route('/get_telemetry', methods=['POST'])
def get_telemetry():
    data = request.json
    race_id = data.get('race_id')
    driver1_id = data.get('driver1_id')
    driver2_id = data.get('driver2_id')

    if not race_id or not driver1_id or not driver2_id:
        return jsonify({"status": "error", "message": "Missing required parameters"})

    # Fetch telemetry data for driver 1
    telemetry1 = db_query("""
        SELECT lap_number, lap_time, speed, acceleration, brake, throttle, gear 
        FROM telemetry 
        WHERE race_id = %s AND driver_id = %s
        ORDER BY lap_number
    """, (race_id, driver1_id))

    # Fetch telemetry data for driver 2
    telemetry2 = db_query("""
        SELECT lap_number, lap_time, speed, acceleration, brake, throttle, gear 
        FROM telemetry 
        WHERE race_id = %s AND driver_id = %s
        ORDER BY lap_number
    """, (race_id, driver2_id))

    if not telemetry1 or not telemetry2:
        return jsonify({"status": "error", "message": "No telemetry data found"})

    return jsonify({
        "status": "success",
        "driver1": telemetry1,
        "driver2": telemetry2
    })
# ------------------------------ LOGOUT ROUTE ------------------------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# ------------------------------ RUN FLASK APP ------------------------------
if __name__ == '__main__':
    app.run(debug=True)