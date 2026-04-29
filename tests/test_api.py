from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_run_and_fetch_result():
    response = client.post(
        "/api/runs",
        json={
            "era_ko": "현대",
            "place_ko": "숲",
            "characters_ko": "토끼, 다람쥐",
            "topic_ko": "우정",
            "tts_enabled": True,
            "scene_count": 4,
            "image_count_per_scene": 3,
        },
    )
    assert response.status_code == 202
    run_id = response.json()["run_id"]

    status_response = client.get(f"/api/runs/{run_id}")
    assert status_response.status_code == 200
    payload = status_response.json()
    assert payload["status"] == "completed"
    assert len(payload["result"]["scenes"]) == 4
    assert len(payload["result"]["images"]) == 12
    assert len(payload["result"]["audio"]) == 4
