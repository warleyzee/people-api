import logging
import pandas as pd

# Chamar funções de utils.py para processar
from utils import avg_age, find_oldest_youngest, invalid_ages, clean_age_column

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


# Ler o CSV
def main() -> None:
    logging.info("Loading CSV file")
    df = pd.read_csv("data/people.csv")

    df = clean_age_column(df)

    oldest, youngest = find_oldest_youngest(df)

    if not oldest.empty:
        logging.info("Oldest person(s):\n%s", oldest[["name", "age"]])

    if not youngest.empty:
        logging.info("Youngest person(s):\n%s", youngest[["name", "age"]])

    logging.info("Average age: %s", avg_age(df))
    logging.info("Names with invalid ages: %s", invalid_ages(df))


if __name__ == "__main__":
    main()
