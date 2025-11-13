import requests

def test_api():
    response = requests.post("http://localhost:5000/predict", json={"age": 45, "symptoms": "fever, cough"})
    assert response.status_code == 200
