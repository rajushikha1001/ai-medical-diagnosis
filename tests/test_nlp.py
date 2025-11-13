from nlp.symptom_parser import extract_symptoms

def test_extract_symptoms():
    assert 'fever' in extract_symptoms("I have fever and cough")
