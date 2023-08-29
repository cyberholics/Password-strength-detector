import requests
import getpass

# Prompt the user to input a password without displaying it
user_password = getpass.getpass("Enter your password: ")

# Specify the URL of your prediction service
url = 'http://localhost:9696/predict'

# Send the POST request with the password as JSON data
response = requests.post(url, json={"user_password": user_password})

# Check the response status code
if response.status_code == 200:
    result = response.json()
    password_strength = result['password_strength']
    if password_strength == 0:
        print("Password Strength is weak!")
    elif password_strength == 1:
        print("Password Strength is ok, but you can make it stronger!")
    elif password_strength == 2:
        print("Password Strength is strong, you are good to go!")
else:
    print("Failed to get a valid response from the prediction service.")

