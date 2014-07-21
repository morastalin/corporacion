
from google.appengine.ext import db


class Publisher(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    city = db.StringProperty()
    state_province = db.StringProperty()
    country = db.StringProperty()
    website = db.StringProperty()

class Author(db.Model):
    salutation = db.StringProperty()
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    email = db.EmailProperty()
    
    def __unicode__(self):
        return self.first_name
    
class Book(db.Model):
    title = db.StringProperty()


class Greeting(db.Model):
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def get_key_from_name(cls, Seguridades_name=None):
        return db.Key.from_path('Seguridades', Seguridades_name or 'default_seguridades')