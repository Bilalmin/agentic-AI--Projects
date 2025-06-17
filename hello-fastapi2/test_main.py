from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_hello_message():
    response = client.get("/chat")
    assert response.status_code == 200
    assert response.json() == {"message": "online class data science"}