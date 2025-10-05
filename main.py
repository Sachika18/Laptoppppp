# main.py — Laptop Price Prediction (Regression Version)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("data.csv")

# -----------------------------
# 🧹 Data Cleaning
# -----------------------------
# Drop unnecessary columns if they exist
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'], errors='ignore')

# Clean RAM column
df['Ram'] = df['Ram'].str.replace('GB', '', regex=False).astype(int)

# Convert ROM column (1TB → 1024GB)
def convert_rom(value):
    value = str(value).upper().replace(' ', '')
    if 'TB' in value:
        return int(float(value.replace('TB', '')) * 1024)
    elif 'GB' in value:
        return int(value.replace('GB', ''))
    else:
        try:
            return int(value)
        except:
            return 0

df['ROM'] = df['ROM'].apply(convert_rom)

# -----------------------------
# 🔠 Label Encoding (for text columns)
# -----------------------------
le_dict = {}
categorical_cols = ['brand', 'processor', 'CPU', 'GPU', 'OS']

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le  # Save encoders for later use in prediction

# -----------------------------
# 🎯 Feature & Target Selection
# -----------------------------
# Keep meaningful columns
X = df[['brand', 'processor', 'CPU', 'Ram', 'ROM', 'GPU', 'OS']]
y = df['price']   # Predict actual numeric price

# -----------------------------
# ✂️ Split Data
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 🤖 Train Model
# -----------------------------
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 📊 Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)
print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# -----------------------------
# 💾 Save Model & Encoders
# -----------------------------
joblib.dump(model, "laptop_price_regression.pkl")
joblib.dump(le_dict, "label_encoders.pkl")

print("✅ Model and encoders saved successfully!")
