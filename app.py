from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dummy fallacy list (for demo purposes)
fallacies = [
    "Ad Hominem", "Strawman", "False Dilemma", 
    "Slippery Slope", "Circular Reasoning", "Appeal to Authority"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    argument = request.form['argument']
    
    # Fake detection logic for now
    detected = random.sample(fallacies, k=2)

    return render_template('index.html', result=detected, argument=argument)

if __name__ == '__main__':
    app.run(debug=True)
