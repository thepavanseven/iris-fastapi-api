import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Load the iris dataset
iris = load_iris(as_frame=True)
X = iris.data
# Rename columns to match the API input names
X.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
y = iris.target

# Build a pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Save the trained model and target names
joblib.dump((pipeline, iris.target_names), "iris_model.pkl")
print("Model trained and saved as iris_model.pkl")
