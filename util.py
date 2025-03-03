import json
import pickle
import numpy as np

__staffExperience = None
__wasteCategory = None
__dataColumns = None
__model = None
__scaler = None

NUMERIC_FEATURES = ["meals_served", "temperature_c", "humidity_percent", "day_of_week", "past_waste_kg"]


def get_estimated_waste(meals_served, temperature_c, humidity_percent, day_of_week, special_event, past_waste_kg, staff_experience, waste_category):

    if __model is None or __scaler is None:
        load_saved_artifacts()

    input_data = np.zeros(len(__dataColumns))

    numeric_values = np.array([[meals_served, temperature_c, humidity_percent, day_of_week, past_waste_kg]])

    if numeric_values.shape[1] != __scaler.n_features_in_:
        raise ValueError(f"Scaler expected {__scaler.n_features_in_} features, but received {numeric_values.shape[1]}.")

    scaled_values = __scaler.transform(numeric_values)[0]

    for i, feature in enumerate(NUMERIC_FEATURES):
        if feature in __dataColumns:
            input_data[__dataColumns.index(feature)] = scaled_values[i]

    if "special_event" in __dataColumns:
        input_data[__dataColumns.index("special_event")] = special_event

    if staff_experience in __dataColumns:
        input_data[__dataColumns.index(staff_experience)] = 1
    if waste_category in __dataColumns:
        input_data[__dataColumns.index(waste_category)] = 1

    estimated_waste = __model.predict([input_data])[0]

    return round(estimated_waste, 2)

def get_staff_experience():
    return __staffExperience


def get_waste_category():
    return __wasteCategory


def load_saved_artifacts():
    print("Loading saved artifacts...")

    global __dataColumns, __staffExperience, __wasteCategory, __model, __scaler

    try:
        with open("./artifacts/columns.json", 'r') as file:
            data = json.load(file)
            __dataColumns = data.get("data_columns", [])

            __staffExperience = [col for col in __dataColumns if "staff_experience" in col]
            __wasteCategory = [col for col in __dataColumns if "waste_category" in col]

    except FileNotFoundError:
        print("Error: columns.json file not found!")

    # Load model
    try:
        with open("./artifacts/RandomForestRegressor_model.pkl", 'rb') as file:
            __model = pickle.load(file)
    except FileNotFoundError:
        print("Error: Model file not found!")

    try:
        with open("./artifacts/minmax_scaler.pkl", "rb") as file:
            __scaler = pickle.load(file)
    except FileNotFoundError:
        print("Warning: Scaler file not found! Ensure correct MinMaxScaler is used.")

    print("Artifacts loaded successfully!")


if __name__ == '__main__':
    load_saved_artifacts()
    print("Staff Experience Categories:", get_staff_experience())
    print("Waste Category Labels:", get_waste_category())
    print(f"Predicted Food Waste (kg): {get_estimated_waste(196, 27.88, 45.36, 0, 0, 7.74, 'staff_experience_beginner', 'waste_category_vegetables')} kg")
