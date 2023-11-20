from .TestClient import CLIENT


def test_get_form():
    url = "/get_form?def_text11=asd&def_some=sss&def_email1=denis.pis@yahoo.com"  # noqa 501
    response = CLIENT.post(url).json()
    assert response == {"finded form": "form122"}
