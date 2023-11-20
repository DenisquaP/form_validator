from .TestClient import CLIENT
from fastapi import status
from random import randint


def test_create_form():
    form = {"form": {
                        "name": f"{randint(1, 1000000)}form`s name",
                        f"field{randint(1, 1000000)}": "1val1"
                    }}
    response = CLIENT.post("/create_form", json=form)
    assert response.status_code == 201
    assert response.json() == {
        "status": status.HTTP_201_CREATED,
        "form": form
    }
