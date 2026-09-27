import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    return df