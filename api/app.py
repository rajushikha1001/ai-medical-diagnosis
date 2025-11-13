from flask import Flask, request, jsonify
from nlp.symptom_parser import extract_symptoms
from ml.disease_predictor import model
from reasoning.triage_engine import triage
from nlp.symptom_parser import extract_symptoms
app = Flask(__name__)

@app.route('/')
def predict():
    data = request.json
    symptoms = extract_symptoms(data['symptoms'])
    risk_score = model.predict_proba([[data['age']]])[0][1]
    decision = triage(symptoms, risk_score)
    return jsonify({"risk_score": risk_score, "triage": decision})

if __name__ == '__main__':
    app.run(debug=True)
