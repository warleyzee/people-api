import pandas as pd
from typing import Tuple, List


def clean_age_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    return df


def avg_age(df: pd.DataFrame) -> int | None:
    valid_df = df.dropna(subset=["age"])

    if valid_df.empty:
        return None

    return round(valid_df["age"].mean())


def find_oldest_youngest(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    valid_df = df.dropna(subset=["age"])

    if valid_df.empty:
        return pd.DataFrame(), pd.DataFrame()

    max_age = valid_df["age"].max()
    min_age = valid_df["age"].min()

    return (
        valid_df[valid_df["age"] == max_age],
        valid_df[valid_df["age"] == min_age],
    )


def invalid_ages(df: pd.DataFrame) -> List[str]:
    return df[df["age"].isna()]["name"].tolist()
