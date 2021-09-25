import mongoengine as db
from bson.objectid import ObjectId

class Posting(db.Document):
    post_name = db.StringField()
    description = db.StringField() 
    post_id = db.ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    def to_json(self):
        return {"post_name" : self.post_name , "description" : self.description, "id" : post_id }
