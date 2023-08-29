# import libraries

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer 
from custom_token import tokens

# Rest of your code

print("libraries imported")

# read and process the data

df = pd.read_csv("data.csv", on_bad_lines='skip')
df=df.dropna()
X=df.drop("strength",axis=1).values.flatten()
y=df["strength"].values
print("data processed")

# Machine learning pipeline

password_clf=Pipeline([("vect",TfidfVectorizer(tokenizer=tokens)),("clf",DecisionTreeClassifier())])
print("model training in progress")
password_clf.fit(X,y)
print("model is trained")
print(password_clf.score(X,y))

# Save the trained model pipeline to a file

with open('password_model.pkl', 'wb') as model_file:
    pickle.dump(password_clf, model_file)

print("pipeline saved")