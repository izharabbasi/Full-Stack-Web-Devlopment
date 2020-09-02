from database import Database
import datetime
import uuid

class Post(object):
    def __init__(self, blog_id, title,content,author,date= datetime.datetime.utcnow(),id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id
        

    def save_to_mongo(self):
        Database.insert(collection='posts',data=self.json())

    def json(self):
        return {
            'blog_id': self.blog_id,
            'title': self.title,
            'content':self.content,
            'author':self.author,
            'id':self.id,
            'date':self.date
        }
    
    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={'id':id})

    @staticmethod
    def from_blog(id):
        return Database.find_one(collection='posts',query={'blog_id': id})
