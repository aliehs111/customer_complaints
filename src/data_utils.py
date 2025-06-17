import pandas as pd
from pathlib import Path

def load_data(path: Path) -> pd.DataFrame:
    """Read CSV and return a DataFrame."""
    df = pd.read_csv(path)
    return df

def check_types(df: pd.DataFrame) -> None:
    """Print dtypes and count missing values."""
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isna().sum())
