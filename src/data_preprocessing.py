import pandas as pd

def preprocess_data(df):
    # Remove customerID se existir
    df = df.drop(columns=["customerID"], errors="ignore")
    
    # Converte TotalCharges para numérico
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    
    # Remove valores nulos
    df = df.dropna()
    
    # Converte Churn para 0/1 se existir
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    
    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)
    
    return df