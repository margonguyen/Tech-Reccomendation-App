import mongoengine as db

class User(db.Document):
    email = db.StringField()    
    password = db.StringField()
    def to_json(self):
        return {"email": self.email,"password": self.password}
