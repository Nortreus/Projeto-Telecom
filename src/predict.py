import pandas as pd
import joblib
from src.data_preprocessing import preprocess_data

model = joblib.load("models/model.pkl")
expected_columns = model.feature_names_in_

def predict_customer_churn(customer_data: dict):
    df = pd.DataFrame([customer_data])
    df_processed = preprocess_data(df)
    
    # 🔹 Garante que todas as colunas esperadas pelo modelo existam
    df_processed = df_processed.reindex(columns=expected_columns, fill_value=0)
    
    prediction = model.predict(df_processed)
    probability = model.predict_proba(df_processed)[:, 1][0]
    return int(prediction[0]), float(probability)