from flask import Flask, request, render_template
import re
import joblib

app = Flask(__name__)

def process_string(input_string):
    # Load the pre-trained model and vectorizer
    model = joblib.load('/Users/aasthasharma/MuseMetrics/model.joblib')
    vectorizer = joblib.load('/Users/aasthasharma/MuseMetrics/vectorizer.joblib')   

    # Get input text from the user
    new_text = input_string

    # Clean the input text using regex
    cleaned_text = re.sub(r'[^\w\s]', '', new_text)  # Remove all non-alphanumeric characters except spaces

    # Transform the cleaned text using the pre-trained vectorizer
    cleaned_text_vec = vectorizer.transform([cleaned_text])

    # Predict the genre using the pre-trained model
    predicted_genre = model.predict(cleaned_text_vec)
    return(f"Predicted Genre: {predicted_genre}")

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ''
    if request.method == 'POST':
        input_string = request.form.get('input_string')
        output = process_string(input_string)
    return render_template('MuseMetricsSite_test.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
