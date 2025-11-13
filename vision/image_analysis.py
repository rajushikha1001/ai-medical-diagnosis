from PIL import Image
import numpy as np
import joblib

def analyze_image(path):
    image = Image.open(path).resize((64, 64)).convert('L')
    data = np.array(image).flatten().reshape(1, -1)
    model = joblib.load('models/image_model.pkl')
    return model.predict(data)[0]
