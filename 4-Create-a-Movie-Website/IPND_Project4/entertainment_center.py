# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "December 23, 1995",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "https://dawsonreviews.files.wordpress.com/2012/10/3-stars.jpg")

avatar = media.Movie("Avatar",
                     "December 16, 2009",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     "https://dawsonreviews.files.wordpress.com/2012/10/4-stars.jpg")

dark_knight = media.Movie("The Dark Knight",
                          "August 6, 2008",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "https://dawsonreviews.files.wordpress.com/2012/10/5-stars.jpg")

ratatouille = media.Movie("Ratatouille",
                          "June 28, 2007",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "https://dawsonreviews.files.wordpress.com/2012/10/2-stars.jpg")

inception = media.Movie("Inception",
                        "July 21, 2010",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "https://dawsonreviews.files.wordpress.com/2012/10/5-stars.jpg")

hunger_games = media.Movie("Hunger Games",
                           "April 4, 2012",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo",
                           "https://dawsonreviews.files.wordpress.com/2012/10/3-stars.jpg")

movies = [inception, toy_story, avatar, ratatouille, dark_knight, hunger_games]
fresh_tomatoes.open_movies_page(movies)
