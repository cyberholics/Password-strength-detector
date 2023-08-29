import pickle
import numpy as np
from flask import Flask, request, jsonify

# Open the saved model
with open('password_model.pkl', 'rb') as model_file:
    loaded_password_clf = pickle.load(model_file)

# Prediction service function for password strength
def predict_password_strength(user_password):
    predicted_strength = loaded_password_clf.predict([user_password])
    return predicted_strength

# Create a Flask app
app = Flask('PasswordStrength')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Check if 'user_password' key exists in the JSON data
        if 'user_password' not in data:
            return jsonify({'error': 'Invalid JSON structure'}), 400

        # Extract the user's password from the JSON data
        user_password = data['user_password']

        # Call the prediction function
        password_strength = predict_password_strength(user_password)

        return jsonify({'password_strength': int(password_strength)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
