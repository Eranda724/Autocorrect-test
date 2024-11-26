from flask import Flask, render_template, request
from dep import Speller

app = Flask(__name__)
speller = Speller(threshold=3)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_correction', methods=['POST'])
def get_correction():
    text = request.form.get('text', '').strip()
    if not text:
        return render_template('index.html', corrected_text="Please enter a valid word.")

    text = text.lower()
    data = speller.get_candidates(text)

    corrected_text = data if data else [('The word is correct!', 0)]
    return render_template('index.html', corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)
