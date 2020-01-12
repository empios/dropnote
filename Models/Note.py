from pymongo import MongoClient



class Note:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.dropnote
        self.Note = self.db.note
        self.Users = self.db.users

    def save_note(self, data):
        self.Note.insert({"content": data.content, "user": data.username})

    def getAll(self):
        all = self.Note.find()
        new_note = []
        for note in all:
            note["user"] = self.Users.find_one({"username": note["user"]})
            new_note.append(note)
        return new_note
