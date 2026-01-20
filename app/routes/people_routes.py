from fastapi import APIRouter, HTTPException

from app.models.people_model import PersonStats, InvalidAgesResponse
from app.services.people_data_source import load_people_df, PeopleDataSourceError
from app.services.people_service import avg_age, find_oldest_youngest, invalid_ages

router = APIRouter()


@router.get("/people/stats", response_model=PersonStats)
def get_people_stats():
    try:
        df = load_people_df()
    except PeopleDataSourceError as exc:

        raise HTTPException(status_code=500, detail=str(exc))

    oldest_df, youngest_df = find_oldest_youngest(df)

    return PersonStats(
        oldest=oldest_df["name"].tolist(),
        youngest=youngest_df["name"].tolist(),
        average_age=avg_age(df),
    )


@router.get("/people/invalid", response_model=InvalidAgesResponse)
def get_invalid_ages():
    try:
        df = load_people_df()
    except PeopleDataSourceError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    return InvalidAgesResponse(invalid_names=invalid_ages(df))
