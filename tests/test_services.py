import pandas as pd
from app.services.people_service import avg_age


def test_avg_age():
    df = pd.DataFrame({"name": ["Ana", "Bob"], "age": [30, 40]})

    result = avg_age(df)
    assert result == 35
