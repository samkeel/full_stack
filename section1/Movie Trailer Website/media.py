class Movie():
    """Creates reusable properties for Movie objects"""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Inits MovieClass with title, poster image link and trailer youtube link."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
