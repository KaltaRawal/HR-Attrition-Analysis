import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

def train_model(df):
    X = df.drop(['Attrition', 'AttritionFlag'], axis=1)
    y = df['AttritionFlag']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8
    )

    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, "attrition_model.pkl")

    return model, X_test, y_test
