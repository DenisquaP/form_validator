from fastapi.testclient import TestClient
from ..main import app

CLIENT = TestClient(app)
