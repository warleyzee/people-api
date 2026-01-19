import pandas as pd
from utils import avg_age, find_oldest_youngest, invalid_ages


# avg_age
def test_avg_age_with_valid_ages():
    df = pd.DataFrame({"name": ["Ana", "Bob", "Carlos"], "age": [20, 30, 40]})

    result = avg_age(df)

    assert result == 30


def test_avg_age_with_only_invalid_ages():
    df = pd.DataFrame({"name": ["Ana", "Bob", "Carlos"], "age": [None, None, None]})

    result = avg_age(df)

    assert result is None


# ✔ find_oldest_youngest
def test_find_oldest_youngest_tie():
    df = pd.DataFrame(
        {"name": ["Camilla", "Joao", "Ana", "Pedro"], "age": [40, 25, 40, 25]}
    )

    oldest, youngest = find_oldest_youngest(df)

    assert set(oldest["name"].tolist()) == {"Camilla", "Ana"}
    assert set(youngest["name"].tolist()) == {"Joao", "Pedro"}


def test_find_oldest_yougest_empty():
    df = pd.DataFrame(columns=["name", "age"])

    oldest, youngest = find_oldest_youngest(df)

    assert oldest.empty
    assert youngest.empty


# ✔ wrong_age
def test_invalid_ages_with_invalid_values():
    df = pd.DataFrame({"name": ["Ana", "Bob", "Carlos"], "age": [20, None, None]})

    result = invalid_ages(df)

    assert set(result) == {"Bob", "Carlos"}


def test_invalid_ages_without_invalid_values():
    df = pd.DataFrame({"name": ["Ana", "Bob", "Carlos"], "age": [20, 30, 40]})

    result = invalid_ages(df)

    assert result == []


# Com idades inválidas

# Sem idades inválidas
