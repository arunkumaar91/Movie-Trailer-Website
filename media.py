class Movie():

    """ This class contains movie related information """
    
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image, movie_trailer_youtube):

        """ __init__ function initializes space in memory
        for the mentioned objects"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube
