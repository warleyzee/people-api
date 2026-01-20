import pandas as pd
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_people_stats(monkeypatch):
    import app.routes.people_routes as people_routes

    def fake_load_people_df():
        return pd.DataFrame({"name": ["A", "B"], "age": [10, 20]})

    # Mock no local onde a rota usa a função
    monkeypatch.setattr(people_routes, "load_people_df", fake_load_people_df)

    response = client.get("/people/stats")
    assert response.status_code == 200
    data = response.json()

    assert data["oldest"] == ["B"]
    assert data["youngest"] == ["A"]
    assert data["average_age"] == 15
