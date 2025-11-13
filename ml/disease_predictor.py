import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('data/patient_records.csv')
X = df[['age']]
y = df['defaulted']

model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, 'models/disease_model.pkl')
