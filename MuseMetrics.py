import numpy as np
import pandas as pd
train = pd.read_csv(r"C:\Users\sathv\OneDrive\Documents\archive (1)\train.csv")
test = pd.read_csv(r"C:\Users\sathv\OneDrive\Documents\archive (1)\test.csv")
train = train[train["Language"] == "en"][["Genre", "Lyrics"]]
test = test[["Genre", "Lyrics"]]
thing = pd.concat([train, test], ignore_index=True)
thing["Lyrics"] = thing["Lyrics"].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
thing["Lyrics"] = thing["Lyrics"].str.replace(r'\n', " ", regex=True)
thing["Lyrics"] = thing["Lyrics"].str.replace(r'\t', " ", regex=True)
real = thing.dropna()

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Assuming 'real' is your DataFrame
X = real['Lyrics']
y = real['Genre']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluate the model
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

#Input
new_lyrics = real.iloc[150239]["Lyrics"]
new_lyrics_vec = vectorizer.transform([new_lyrics])
predicted_genre = model.predict(new_lyrics_vec)
print(f"Predicted Genre: {predicted_genre}")