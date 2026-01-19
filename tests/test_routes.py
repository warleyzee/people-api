from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_people_stats():
    response = client.get("/people/stats")
    assert response.status_code == 200

    data = response.json()
    assert "oldest" in data
    assert "youngest" in data
    assert "avg_age" in data
