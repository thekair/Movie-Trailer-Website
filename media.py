class Movie():
    """This class is a blueprint intended to create movie objects with similar attributes


     Attributes:
        title: A string indicating movie title.
        storyline: A string indicating movie storyline.
        poster_image_url: A string indicating movie poster image url.
        trailer_youtube_url: A string indicating movie trailer youtube url.
    """
    
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """ A constructor for the movie class so that we can create instances of movie """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


