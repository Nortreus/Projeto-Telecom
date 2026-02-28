from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from data_preprocessing import load_data, preprocess_data

# Carregar e processar dados
df = load_data("../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df = preprocess_data(df)

# Separar features e target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Avaliar
preds = model.predict(X_test)
print(classification_report(y_test, preds))

# Salvar modelo
joblib.dump(model, "../models/model.pkl")