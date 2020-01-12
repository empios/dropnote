from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.dropnote
        self.Users = self.db.users

    def save_user(self, data):
        hashes = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        self.Users.insert({"username": data.username, "email": data.email, "password": hashes})
