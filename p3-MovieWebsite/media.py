# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    """This is a class which we are using to store movie related information"""

    # This class provides a way to store movie related information
    #title
    #story line
    #poster
    #trailer link
    # _ _ two underscore is used to tell that init is python keyword it is already redeclared
    #self is pointing to that object only for eg if toystory object is created then self mean toystory

    def __init__(self,movie_title, director_name, poster_image, trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.director = director_name
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
