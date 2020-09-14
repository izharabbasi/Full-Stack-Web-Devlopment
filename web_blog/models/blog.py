from web_blog.models.post import Post
from database.database import Database
import datetime
import uuid

class Blog(object):
    def __init__(self,author,title,description,author_id, _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id
        

    def new_post(self,title,content,data= datetime.datetime.utcnow()):
        post = Post(
            blog_id=id,
            title=title,
            content=content,
            author=self.author,
            date= data
        )
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blog',data=self.json())

    def json(self):
        return {
            'author' : self.author,
            'author_id': self.author_id,
            'title' : self.title,
            'description' : self.description,
            '_id' : self._id 
        }
    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one(collection='blog',query={'_id':id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls,author_id):
        blogs = Database.find(collection='blogs', query={'author_id':author_id})    

        return [cls(**blog) for blog in blogs]
        

    