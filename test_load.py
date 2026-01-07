# test_load.py
import joblib
from my_transformers import DateTransformer

print("START")

model = joblib.load("fraud_model.pkl")

print("MODEL LOADED")
print(type(model))
