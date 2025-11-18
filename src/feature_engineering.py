import pandas as pd
import numpy as np

def add_features(df):
    df = df.copy()

    # Numeric attrition flag
    df['AttritionFlag'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    # Engagement Score
    df['EngagementScore'] = (
        df['JobSatisfaction'] +
        df['WorkLifeBalance'] +
        df['ManagerRating']
    ) / 3

    # Work Strain Score
    df['WorkStrainScore'] = (
        df['OverTimeHours'] * 0.6 +
        df['DistanceFromHome'] * 0.4
    )

    # ManagerLow flag
    df['ManagerLow'] = (df['ManagerRating'] <= 2).astype(int)

    # Tenure Buckets
    df['TenureBucket'] = pd.cut(
        df['YearsAtCompany'],
        bins=[0,1,5,50],
        labels=['Early', 'Mid', 'Senior']
    )

    return df
