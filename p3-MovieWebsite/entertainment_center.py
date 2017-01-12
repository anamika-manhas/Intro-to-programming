# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

suicide_squad = media.Movie("Suicide Squad",
                        "David Ayer",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png",
                        "https://www.youtube.com/watch?v=smHxeRdf7oI")

wonder_woman = media.Movie("Wonder Woman",
                     "Patty Jenkins",
                     "http://ia.media-imdb.com/images/M/MV5BMTU2ODQ1OTUyOF5BMl5BanBnXkFtZTgwMjc2MzE1OTE@._V1_SY1000_SX675_AL_.jpg",
                     "https://www.youtube.com/watch?v=5lGoQhFb4NM")

storks = media.Movie("Storks",
                     "Nicholas Stoller, Doug Sweetland",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Storks_%28film%29_poster_2.jpg",
                     "https://www.youtube.com/watch?v=3ubGgmaexv8")

lights_out = media.Movie("Lights Out",
                     "David F. Sandberg",
                     "https://upload.wikimedia.org/wikipedia/en/d/dc/Lights_Out_2016_poster.jpg",
                     "https://www.youtube.com/watch?v=H_nTMprod00")

dr_strange = media.Movie("Doctor Strange",
                     "Scott Derrickson",
                     "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                     "https://www.youtube.com/watch?v=HSzx-zryEgM")

kong = media.Movie("Kong: Skull Island",
                     "Jordan Vogt-Roberts",
                     "https://upload.wikimedia.org/wikipedia/en/8/87/Kong_Skull_Island_SDCC16.jpg",
                     "https://www.youtube.com/watch?v=YAbI4w95cTE")

movies = [suicide_squad, wonder_woman, storks, lights_out, dr_strange, kong]
fresh_tomatoes.open_movies_page(movies)
#It uses the list of movies to create page and open Html webpage
