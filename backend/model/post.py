import mongoengine as db

class Posting(db.Document):
    post_name = db.StringField()    
    def to_json(self):
        return {"post_name" : self.post_name}
