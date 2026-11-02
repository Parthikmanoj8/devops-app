from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.get_json() == {"status": "UP"}

def test_about():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200
