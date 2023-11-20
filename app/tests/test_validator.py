from ..validators.validator import type_of
import pytest


@pytest.mark.asyncio
async def test_type_of_text():
    res = await type_of("asd")
    assert res == "text"


@pytest.mark.asyncio
async def test_type_of_phone():
    res = await type_of("+79651231213")
    assert res == "phone"


@pytest.mark.asyncio
async def test_type_of_email():
    res = await type_of("denis.pis@yahoo.com")
    assert res == "email"
