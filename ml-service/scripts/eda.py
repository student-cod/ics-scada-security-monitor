import pandas as pd

df = pd.read_csv("../data/merged.csv")

print("Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nFirst few rows:\n", df.head())

# SWaT datasets usually have a label column called 'Normal/Attack'
label_col = [c for c in df.columns if "attack" in c.lower() or "label" in c.lower()]
print("\nPossible label column(s):", label_col)

if label_col:
    print("\nClass distribution:\n", df[label_col[0]].value_counts())