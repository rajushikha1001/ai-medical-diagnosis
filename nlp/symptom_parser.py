import re

def extract_symptoms(text):
    symptoms = re.findall(r'\b(fever|cough|fatigue|chest pain|short breath|headache|nausea)\b', text.lower())
    return list(set(symptoms))
