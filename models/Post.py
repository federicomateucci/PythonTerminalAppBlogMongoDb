import uuid
import Database
import datetime

class Post(object):


    def __init__(self, blog_id, tittle, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.tittle = tittle
        self.content = content
        self.author = author
        self.date = date
        # importo el modulo uuid que genera una ID nueva y aleatoria para cada post.
        # pero solo si genero un post por primera vez , si no utiliza mi id ya creada.
        self.id = uuid.uuid4().hex if id is None else id



    def save_to_mongo(self):
        Database.Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'tittle' : self.tittle,
            'date'  : self.date
        }
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.Database.find_one(collection='posts', query={'id' : id})
        return cls(blog_id=post_data['blog_id'],
                   tittle=post_data['tittle'],
                   content=post_data['content'],
                   id=post_data['id'],
                   date=post_data['date'])


    @staticmethod
    def from_blog(id):
        return [post for post in Database.Database.find(collection='posts', query={'blog_id' : id})]










