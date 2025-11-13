def triage(symptoms, risk_score):
    if 'chest pain' in symptoms or risk_score > 0.7:
        return "High urgency: Immediate medical attention required"
    elif 'fever' in symptoms:
        return "Medium urgency: Schedule a checkup"
    else:
        return "Low urgency: Monitor at home"
