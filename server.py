from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/get_staff_experience')
def get_staff_experience():
    response = jsonify({
        'staff_experience': util.get_staff_experience()
    })
    return response

@app.route('/get_waste_category')
def get_waste_category():
    response = jsonify({
        'waste_category': util.get_waste_category()
    })
    return response

@app.route('/predict_food_waste', methods=['POST'])
def predict_food_waste():
    data = request.json  # Use request.json instead of request.form

    meals_served = int(data['mealsServed'])
    temperature_c = float(data['temperature'])
    humidity_percent = float(data['humidity'])
    day_of_week = data['dayOfWeek']
    special_event = 1 if data['specialEvent'] else 0
    past_waste_kg = float(data['pastWaste'])
    staff_experience = data['staffExperience']
    waste_category = data['wasteCategory']

    # Convert categorical values
    day_of_week_mapping = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
        'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    staff_experience_mapping = {
        'Beginner': 'staff_experience_beginner',
        'Intermediate': 'staff_experience_intermediate',
        'Expert': 'staff_experience_expert'
    }
    waste_category_mapping = {
        'Dairy': 'waste_category_dairy',
        'Meat': 'waste_category_meat',
        'Vegetables': 'waste_category_vegetables',
        'Grains': 'waste_category_grains'
    }

    day_of_week = day_of_week_mapping.get(day_of_week, 6)  # Default to Sunday
    staff_experience = staff_experience_mapping.get(staff_experience, 'staff_experience_expert')
    waste_category = waste_category_mapping.get(waste_category, 'waste_category_grains')

    prediction = util.get_estimated_waste(
        meals_served, temperature_c, humidity_percent, day_of_week,
        special_event, past_waste_kg, staff_experience, waste_category
    )

    response = jsonify({'prediction': prediction})
    return response

if __name__ == "__main__":
    print("Starting Python Flask server for Food Waste Prediction...")
    util.load_saved_artifacts()
    app.run()