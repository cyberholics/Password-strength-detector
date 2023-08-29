## Introduction

Passwords play a crucial role as the first line of defence in safeguarding the security of an application. When a password is compromised, it can have severe repercussions for the overall security of the application and its users.

A strong password is characterised by its complexity, length, and uniqueness. It typically includes a combination of uppercase and lowercase letters, numbers, and special characters. Additionally, it should be unique to each user and not be shared or reused across multiple accounts or applications.
When users choose weak or easily guessable passwords, they inadvertently expose the application to potential security breaches. These breaches can lead to unauthorised access, data theft, or other malicious activities that can harm both the application and its users.

To enhance application security, it's crucial to encourage users to create strong, unique passwords.
This can be done with the help of artificial intelligence (AI), as an AI model can learn what constitutes a strong or weak password and assist users in detecting whether their password is weak or not. In this project, I have developed an AI system to address this issue. To learn more about this solution, visit this [blog](https://dev.to/cyber_holics/password-strength-detector-with-machine-learning-3m5g).

## Project key files explained

- **password strength detector.ipynb:** This is a Jupyter notebook where I performed exploratory data analysis (EDA) on the data, preprocessed the data, and trained my model.
  
- **data.csv:** This is a dataset of 690 thousand samples of passwords stored in a comma-separated value (CSV) format. I used data to train the AI model.

- **password_model.pkl:** This is the saved model that will be used for the prediction.

- **train.py:** This is a Python script that trains and saves the model.

- **predict.py:** This is the Flask app to run the prediction service.

- **request.py:** This script sends a request to the web service(predict.py) which accepts user's password as input and returns a prediction of whether the password is weak,strong, or medium.

- **Pipfile & Pipfile.lock:** These are dependencies management files used to create a virtual environment for the machine learning project. This is to ensure the reproducibility of the project.

## Running the project

Running this project requires you to be familiar with the command line; Navigate to you command line and run the following commnad. 
1) Clone this repo: `git clone https://github.com/cyberholics/Password-strength-detector.git`
2) Enter the project directory: cd `Password-strength-detector`
3) Create a virtual environment with dependencies:`pipenv install`
4) Run the training script: `python train.py` 
5) Get predictions with the trained model: `predict.py`
6) Send the user password as input to get a prediction: From another terminal session in the project directory, run `python request.py`




## Project Demo
I tried  `heyhey`
![Weak password](https://github.com/cyberholics/Password-strength-detector/blob/main/weak%20password.png)

I tried `heyheyQ@11` 
![Medium password](https://github.com/cyberholics/Password-strength-detector/blob/main/meduim%20pass.png)

I tried `sakaryal&#305;` 
![Strong password](https://github.com/cyberholics/Password-strength-detector/blob/main/strong%20password.png)
