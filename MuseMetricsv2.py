import re
import joblib

# Load the pre-trained model and vectorizer
model = joblib.load('/Users/aasthasharma/MuseMetrics/model.joblib')
vectorizer = joblib.load('/Users/aasthasharma/MuseMetrics/vectorizer.joblib')

# Get input text from the user
new_text = input("Enter text to classify its genre: ")

# Clean the input text using regex
cleaned_text = re.sub(r'[^\w\s]', '', new_text)  # Remove all non-alphanumeric characters except spaces

# Transform the cleaned text using the pre-trained vectorizer
cleaned_text_vec = vectorizer.transform([cleaned_text])

# Predict the genre using the pre-trained model
predicted_genre = model.predict(cleaned_text_vec)
print(f"Predicted Genre: {predicted_genre}")

