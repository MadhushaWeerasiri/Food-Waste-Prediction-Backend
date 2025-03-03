# Food Waste Prediction - Backend

This is a Flask-based server application for handling requests related to food waste predictions.

## Features
- REST API using Flask
- CORS support for cross-origin requests
- Handles requests for staff experience and waste category
- Utilizes a trained model for waste estimation

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions
1. Clone this repository or extract `Server.zip`.
2. Navigate to the extracted `Server` folder:
   ```bash
   cd Server
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask server:
   ```bash
   python server.py
   ```
2. The server will start, and you can access it at:
   ```
   http://127.0.0.1:5000/
   ```
3. Available API endpoints:
   - `GET /hello` - Returns a simple greeting.
   - `GET /get_staff_experience` - Retrieves staff experience data.
   - `GET /get_waste_category` - Retrieves waste category data.

## Dependencies
- Flask
- Flask-CORS
- NumPy

## Contributing
Feel free to fork this repository and submit pull requests.

## Contact
Mail: mdweerasiri@gmail.com
Linkedin: https://www.linkedin.com/in/madhushaweerasiri/

