from fastapi import FastAPI, Form
import csv

app = FastAPI()

class User_DB:
    def __init__(self, path: str):
        self.path = path
        self.user_fields = []
        self.user_rows = []
        try:
            with open(path, "r", newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                self.user_fields = next(csvreader)
                for row in csvreader:
                    if row:
                        self.user_rows.append(row)
        except:
            with open(path, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["username", "password"])
            self.user_fields = ["username", "password"]
            self.user_rows = []

    def save_user(self, username, password):
        with open(self.path, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
        self.user_rows.append([username, password])

    def get_users(self):
        return [{"username": row[0], "password": row[1]} for row in self.user_rows]

temp_user_db = User_DB("user_db.csv")

def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_special = False
    if 5 <= len(password) <= 20:
        for c in password:
            if c.isupper():
                has_upper = True
            elif c.islower():
                has_lower = True
            elif c in ('@', '_'):
                has_special = True
        return has_upper and has_lower and has_special
    return False

@app.get("/users")
def get_users():
    return temp_user_db.get_users()

@app.post("/users")
def add_user(
    username: str = Form(...),
    password: str = Form(...)
):
    if not username or not password:
        return {"error": "Username and password are required."}

    for user in temp_user_db.user_rows:
        if user[0] == username:
            return {"error": "Username already exists."}

    if not is_valid_password(password):
        return {"error": "Password must be 5-20 characters long, include uppercase, lowercase, and '@' or '_'."}

    temp_user_db.save_user(username, password)
    return {
    "message": "Uploaded user successfully",
    "user": username,
    "password": password
}
