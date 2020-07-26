__author__ = 'federico mateucci'

from Database import Database
from models.Blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name : ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()


    def _user_has_account(self):
         datainfoblog = Database.find_one('blogs', {'author': self.user})  # Check in database if user exists, and throws a boolean
         if datainfoblog is not None:
             self.user_blog = Blog.get_from_mongo(datainfoblog['id'])
             return True
         else:
             return False


    def _prompt_user_for_account(self):
        tittle = input("enter blog title : ")
        description = input("Enter blog description")
        blog = Blog(author=self.user,
                    tittle=tittle,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs?")
        antiCrashDecision = read_or_write.upper()
        if antiCrashDecision == 'R':
            self._list_blogs()
            self._view_blog()
        elif antiCrashDecision == 'W':
            self.user_blog.new_post()
        else:
            print("Thansk You For Blogging !")



    def _prompt_write_post(self):
        self.user_blog.new_post()


    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID:{}, Tittle: {}, Author: {}".format(blog['id'], blog['tittle'], blog['author']))


    def _view_blog(self):
        blog_to_see = input("Enter ID of your blog you like it to read")
        blog = Blog.get_from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date : {}, Tittle: {}\n\n{}".format(post['date'], post['tittle'], post['content']))

