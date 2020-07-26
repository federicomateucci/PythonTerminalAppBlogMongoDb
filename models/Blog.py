import uuid
import datetime

from Database import Database
from models.Post import Post

__author__: 'Federico Mateucci'


class Blog(object):
    def __init__(self, author, tittle, description, id=None):
        self.author = author
        self.tittle = tittle
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        tittle = input("Enter post Tittle: ")
        content = input("Enter post Content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY ): ")
        if date == "":
            date = datetime.datetime.utcnow() # put localmachineDate in Date with DateFormat
        else:
           date=datetime.datetime.strptime(date, "%d%m%Y") #parse str to DateFormat

        post = Post(blog_id=self.id,
                    tittle=tittle,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()

    def get_posts(self):  # este metodo es igual que el que efectuamos en la clase Post , metodo : from_blog(id)
        return Post.from_blog(
            self.id)  # reutilizamos el metodo para devolver los post por ID , en este caso devuelve los post del mismo blog

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self): #convert to json for later save this to mongoDB
        return {
            'author': self.author,
            'tittle': self.tittle,
            'description': self.description,
            'id': self.id

        }

    @classmethod
    def get_from_mongo(cls, id):  # return his own class object
        blog_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(author=blog_data['author'],
                   tittle=blog_data['tittle'],
                   description=blog_data['description'],
                   id=blog_data['id'])
