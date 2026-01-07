# test_load.py
import joblib
import transformers

print("START")

model = joblib.load("fraud_model.pkl")

print("MODEL LOADED")
print(type(model))
