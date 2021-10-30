import mongoengine as db
from model.posting import Posting

class User(db.Document):
    email = db.StringField()    
    password = db.StringField()
    name = db.StringField()
    stack = db.ListField()
    description = db.StringField()
    projects = db.ListField(db.ReferenceField(Posting))
    def to_json(self):
        return {"name" : self.name, "description" : self.description , "email": self.email,"password": self.password, "stack" : self.stack }