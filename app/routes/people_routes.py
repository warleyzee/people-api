from fastapi import APIRouter
import pandas as pd
from app.services.people_service import (
    clean_age_column,
    avg_age,
    find_oldest_youngest,
    invalid_ages,
)
from app.models.people_model import PersonStats, InvalidAgesResponse

router = APIRouter()

DATA_PATH = "data/people.csv"


@router.get("/people/stats", response_model=PersonStats)
def get_people_stats():
    df = pd.read_csv(DATA_PATH)
    df = clean_age_column(df)

    oldest_df, youngest_df = find_oldest_youngest(df)

    oldest_names = oldest_df["name"].tolist()
    youngest_names = youngest_df["name"].tolist()

    return PersonStats(
        oldest=oldest_names, youngest=youngest_names, avg_age=avg_age(df)
    )


@router.get("/people/invalid", response_model=InvalidAgesResponse)
def get_invalid_ages():
    df = pd.read_csv(DATA_PATH)
    df = clean_age_column(df)
    return InvalidAgesResponse(invalid_names=invalid_ages(df))
