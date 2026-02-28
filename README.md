# Projeto Previsão de Churn - Telecom

## 🔹 Descrição

Este projeto implementa um modelo de **machine learning** para prever a **probabilidade de churn de clientes de uma empresa de telecomunicações**.  
O modelo foi treinado com dados reais de clientes, e a API foi construída com **FastAPI**, permitindo previsões via requisições HTTP.

---

## 🔹 Estrutura do projeto


churn-prediction/
│
├── app.py # API FastAPI
├── models/
│ └── model.pkl # Modelo treinado
├── src/
│ ├── predict.py # Função de previsão
│ └── data_preprocessing.py# Pré-processamento dos dados
├── notebooks/ # Notebooks para análise e treinamento
├── test_request.json # Exemplo de JSON para teste da API
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo


---

## 🔹 Tecnologias utilizadas

- Python 3.14  
- Pandas, NumPy  
- Scikit-learn  
- FastAPI  
- Uvicorn  

---

## 🔹 Como rodar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Nortreus/Projeto-Telecom.git
cd Projeto-Telecom
2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
3️⃣ Instalar as dependências
pip install -r requirements.txt
4️⃣ Rodar a API
uvicorn app:app --reload

A API vai rodar em: http://127.0.0.1:8000

Documentação interativa em: http://127.0.0.1:8000/docs

🔹 Exemplo de requisição /predict

Arquivo test_request.json:

{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.35,
  "TotalCharges": 845.5
}

Resposta esperada:

{
  "churn_prediction": 0,
  "churn_probability": 0.23
}
🔹 Teste rápido via terminal
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @test_request.json
🔹 Observações

A função de pré-processamento garante que os dados do cliente sejam convertidos para o formato esperado pelo modelo.

O modelo (model.pkl) foi treinado com one-hot encoding das variáveis categóricas.

Caso novas features sejam adicionadas ao modelo, é necessário atualizar src/predict.py para compatibilidade.