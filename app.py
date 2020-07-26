__author__ = 'federico mateucci'

#import pymongo
from Menu import Menu
from models.Blog import Blog
from models.Post import Post
from Database import Database


#uri = "mongodb://127.0.0.1:27017"
#cliente = pymongo.MongoClient(uri)
#database = cliente['fullstack']
#collection = database['students']

#tudents = collection.find({})

#for studen in students:
 #   print(studen)


Database.initialize()

menu = Menu()

menu.run_menu()

