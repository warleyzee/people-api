from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd

from app.services.people_service import clean_age_column


@dataclass(frozen=True)
class PeopleDataSourceError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


def load_people_df(csv_path: str | Path = "data/people.csv") -> pd.DataFrame:

    path = Path(csv_path)

    if not path.exists():
        raise PeopleDataSourceError(f"People CSV not found at: {path}")

    try:
        df = pd.read_csv(path)
    except Exception as exc:
        raise PeopleDataSourceError(f"Failed to read People CSV: {exc}")

    required_cols = {"name", "age"}
    missing = required_cols - set(df.columns)
    if missing:
        raise PeopleDataSourceError(
            f"Invalid People CSV. Missing required column(s): {sorted(missing)}"
        )

    df = clean_age_column(df)
    return df
