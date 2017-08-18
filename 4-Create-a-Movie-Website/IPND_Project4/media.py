# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    ''' This class provides a way to story movie related information '''
    # define valid rating
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # initialize instance of class Movie
    def __init__(self, movie_title, release_date, poster_image, trailer_youtube, movie_rate):
        self.title = movie_title
        self.release_date = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rate = movie_rate

    def show_trailer(self):
        ''' This function open webbrowser and show movie trailer each '''
        webbrowser.open(self.trailer_youtube_url)
