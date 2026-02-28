import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    # Remover coluna de ID
    df = df.drop(columns=["customerID"])
    
    # Corrigir TotalCharges
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna()
    
    # Transformar target em 0/1
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    
    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)
    
    return df