from .TestClient import CLIENT


def test_get_forms():
    response = CLIENT.get("/doc_count")
    assert response.status_code == 200
