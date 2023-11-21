from fastapi import status
from random import randint
import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_create_form(async_client: AsyncClient):
    form = {"form": {
                        "name": f"{randint(1, 1000000)}form`s name",
                        f"field{randint(1, 1000000)}": "1val1"
                    }}
    response = await async_client.post("/create_form", json=form)
    assert response.status_code == 201
    assert response.json() == {
        "status": status.HTTP_201_CREATED,
        "form": form
    }


@pytest.mark.anyio
async def test_get_forms(async_client: AsyncClient):
    response = await async_client.get("/doc_count")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_form(async_client: AsyncClient):
    url = "/get_form?def_text11=asd&def_some=sss&def_email1=denis.pis@yahoo.com"  # noqa 501
    response = await async_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"finded form": "form122"}


@pytest.mark.asyncio
async def test_get_form_REST(async_client: AsyncClient):
    body = {
        "def_text11": "text",
        "def_email1": "denis.pis@yahoo.com"
    }
    response = await async_client.post("/get_form_REST", json=body)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"finded form": "form122"}
