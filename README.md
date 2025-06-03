# 🔐 Login Page – Unit Testing with FastAPI & Pytest

Welcome to the **Login Page** unit testing project!  
This project demonstrates how to use **FastAPI** to create a simple login API with `GET` and `POST` methods and how to perform **automated unit testing** using **pytest** and **requests**.

---

## 🚀 Features

- ✅ FastAPI-based RESTful API
- ✅ `POST` method for user login
- ✅ `GET` method to retrieve user data
- ✅ Unit testing with `pytest`
- ✅ Test coverage for:
  - Valid login
  - Duplicate usernames
  - Invalid password formats
  - Fetching all users

---

## 🛠️ Tech Stack

- 🐍 Python 3.9+
- ⚡ FastAPI
- 🔬 Pytest
- 🌐 Requests library

---

## 🧪 Testing Highlights

This project includes **automated test cases** for the following scenarios:

- 🔄 **User Fetching**  
  `GET /users` – Fetch a list of all users

- ➕ **Successful User Addition**  
  `POST /users` – Add a new user with valid credentials

- ❌ **Duplicate Username**  
  Prevent creation of accounts with an existing username

- 🔒 **Weak Password Detection**  
  Enforce password strength rules (length, uppercase, symbols, etc.)

---

## 🧾 Sample Test Code Snippet

```python
def test_add_user_success():
    payload = {"username": "testuser", "password": "Test@123"}
    response = requests.post(f"{BASE_URL}/users", data=payload)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Uploaded user successfully",
        "user": payload["username"],
        "password": payload["password"]
    }
