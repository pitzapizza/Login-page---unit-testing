import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"  # Ensure FastAPI is running before testing

@pytest.fixture
def sample_user():
    return {"username": "testuser", "password": "Test@123"}

def test_get_users():
    """Test fetching users"""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure response returns a list

def test_add_user_success(sample_user):
    """Test successful user addition"""
    response = requests.post(f"{BASE_URL}/users", data=sample_user)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Uploaded user successfully",
        "user": sample_user["username"],
        "password": sample_user["password"]
    }

def test_add_user_existing_username():
    """Test duplicate username prevention"""
    payload = {"username": "duplicateuser", "password": "Test@123"}
    requests.post(f"{BASE_URL}/users", data=payload)  # First request
    response = requests.post(f"{BASE_URL}/users", data=payload)  # Duplicate request
    assert response.status_code == 200
    assert response.json() == {"error": "Username already exists."}

def test_add_user_invalid_password():
    """Test password validation"""
    payload = {"username": "weakuser", "password": "weak"}
    response = requests.post(f"{BASE_URL}/users", data=payload)
    assert response.status_code == 200
    assert response.json() == {"error": "Password must be 5-20 characters long, include uppercase, lowercase, and '@' or '_'."}
