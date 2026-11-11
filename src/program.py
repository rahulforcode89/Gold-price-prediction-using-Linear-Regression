# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from pathlib import Path

print("Libraries imported successfully!")

# 2. Read Dataset
script_dir = Path.cwd()
file_path = "../data/gold_price_data.csv"
df = pd.read_csv(file_path)
print("Dataset shape (rows, columns):", df.shape)
print(df.head())

# 3. Explore the Data with Graphs
# Histogram of target Gold price (Adj Close)
column_to_plot = "Adj Close"
plt.figure(figsize=(8, 4))
plt.hist(df[column_to_plot].dropna(), bins=20, color="gold", edgecolor="black")
plt.title(f"Distribution of {column_to_plot}")
plt.xlabel(column_to_plot)
plt.ylabel("Frequency")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("../outputs/gold_price_distribution.png")
plt.show()
print("Saved outputs/gold_price_distribution.png")

# Scatter plot: GDX_Close vs Adj Close
feature_for_plot = "GDX_Close"
target_for_plot = "Adj Close"
plt.figure(figsize=(8, 5))
plt.scatter(df[feature_for_plot], df[target_for_plot], alpha=0.65)
plt.title(f"{target_for_plot} vs {feature_for_plot}")
plt.xlabel(feature_for_plot)
plt.ylabel(target_for_plot)
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("../outputs/feature_vs_gold_scatter.png")
plt.show()
print("Saved outputs/feature_vs_gold_scatter.png")

# 4. Preprocess the Data
df = df.drop_duplicates().copy()

target_column = "Adj Close"
gld_columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
feature_columns = [col for col in df.columns if col not in gld_columns]

model_df = df[feature_columns + [target_column]].copy()
model_df[target_column] = pd.to_numeric(model_df[target_column], errors="coerce")
model_df = model_df.dropna(subset=[target_column])

X = model_df[feature_columns]
y = model_df[target_column]

numeric_features = X.select_dtypes(include=np.number).columns.tolist()
categorical_features = X.select_dtypes(exclude=np.number).columns.tolist()

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("numeric", numeric_transformer, numeric_features),
    ("categorical", categorical_transformer, categorical_features)
])

print("Input shape:", X.shape)
print("Target shape:", y.shape)
print("Rows available for modelling:", len(model_df))

# 5. Split into Training and Testing Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42
)

print("Training examples:", len(X_train), "(80 percent of total data)")
print("Testing examples:", len(X_test), "(20 percent of total data)")

# 6. Building and Training the Linear Regression Model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

model.fit(X_train, y_train)
print("Model training completed!")

# 7. Make Predictions
y_pred = model.predict(X_test)

comparison = pd.DataFrame({
    "Actual Price": y_test.to_numpy(),
    "Predicted Price": y_pred,
    "Error (Actual - Predicted)": y_test.to_numpy() - y_pred
})
print(comparison.head(10))

# 8. Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE      : {mae:,.3f}")
print(f"MSE      : {mse:,.3f}")
print(f"RMSE     : {rmse:,.3f}")
print(f"R² score : {r2:.3f}")

# 9. Visualize Actual vs Predicted Prices
plt.figure(figsize=(7, 6))
plt.scatter(y_test, y_pred, alpha=0.7, edgecolor="black")

low = min(float(np.min(y_test)), float(np.min(y_pred)))
high = max(float(np.max(y_test)), float(np.max(y_pred)))
plt.plot([low, high], [low, high], linestyle="--", color="red", label="Perfect prediction")

plt.xlabel("Actual Gold Price")
plt.ylabel("Predicted Gold Price")
plt.title("Actual vs Predicted Gold Prices")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("../outputs/predicted_vs_actual.png")
plt.show()
print("Saved outputs/predicted_vs_actual.png")

# 10. Correlation and Heatmap
number_cols = ["Adj Close", "SP_close", "DJ_close", "GDX_Close", "USO_Close", "USDI_Price", "SF_Price", "USB_Price"]
corr = df[number_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation between numeric columns")
plt.tight_layout()
plt.savefig("../outputs/correlation_heatmap.png")
plt.show()
print("Saved outputs/correlation_heatmap.png")

print("Correlation with Adj Close:")
print(corr["Adj Close"].drop("Adj Close").sort_values(ascending=False).round(2))
