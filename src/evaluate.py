import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import random

def load_data(path="data/splits/clean_data.csv"):
    return pd.read_csv(path)

def dummy_model_predict(texts):
    """
    A fake model that randomly guesses 'cyberbullying' or 'not_cyberbullying'.
    Replace this with Sonika's real model later.
    """
    return [random.choice(["cyberbullying", "not_cyberbullying"]) for _ in texts]

if __name__ == "__main__":
    # Load cleaned dataset
    df = load_data()
    y_true = df["label"]
    y_pred = dummy_model_predict(df["clean_text"])

    # Evaluate
    print("📊 Evaluation Metrics")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("\nClassification Report:\n", classification_report(y_true, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))
