from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_customer_churn

# Definir modelo de entrada
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# Criar app FastAPI
app = FastAPI(title="Churn Prediction API")

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "API de Previsão de Churn funcionando!"}

# Rota de previsão
@app.post("/predict")
def predict(data: CustomerData):
    prediction, probability = predict_customer_churn(data.dict())
    return {
        "churn_prediction": prediction,
        "churn_probability": probability
    }