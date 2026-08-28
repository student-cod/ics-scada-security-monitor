import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import joblib
import os

# ---- 1. Load ----
print("Loading data...")
df = pd.read_csv("../data/merged.csv")
df.columns = df.columns.str.strip()

# ---- 2. Clean: drop unreliable columns instead of dropping rows ----
problem_cols = ["MV101", "MV201", "P201", "P202", "AIT201", "P204", "MV303"]
df = df.drop(columns=problem_cols, errors="ignore")
print(f"Dropped {len(problem_cols)} unreliable columns. Shape now:", df.shape)

df = df.drop_duplicates()
if "Timestamp" in df.columns:
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce", dayfirst=True)

# Check remaining missing values (should now be ~0 or very few)
remaining_missing = df.isnull().sum().sum()
print("Remaining missing cells:", remaining_missing)
df = df.dropna()  # safe now — should barely drop anything
print("Final cleaned shape:", df.shape)

# ---- 3. Separate features and label ----
label_col = "Normal/Attack"
X = df.drop(columns=[label_col, "Timestamp"], errors="ignore")
y = df[label_col].apply(lambda x: 0 if str(x).strip() == "Normal" else 1)