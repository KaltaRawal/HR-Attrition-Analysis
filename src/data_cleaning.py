import pandas as pd

def clean_data(df):
    df = df.copy()

    # Standardize categorical values
    df.columns = df.columns.str.strip()
    df['Department'] = df['Department'].str.strip().str.title()

    # Handle missing numerical values
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)

    # Handle missing categorical values
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df
