import pandas as pd
import joblib

# Check where the missing values actually are
df = pd.read_csv("../data/merged.csv")
df.columns = df.columns.str.strip()
print("Missing values by column (top 15):")
print(df.isnull().sum().sort_values(ascending=False).head(15))

# Check what the model is relying on most heavily
xgb = joblib.load("../models/xgboost_model.pkl")
label_col = "Normal/Attack"
feature_names = df.drop(columns=[label_col, "Timestamp"], errors="ignore").columns
importances = pd.Series(xgb.feature_importances_, index=feature_names).sort_values(ascending=False)
print("\nTop 10 most important features:")
print(importances.head(10))