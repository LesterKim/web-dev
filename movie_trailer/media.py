import webbrowser

class Movie():
    # Movie ratings
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    
    # Initialize class variables
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    # Allow Movie to open trailer in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)