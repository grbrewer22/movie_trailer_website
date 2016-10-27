import webbrowser

# Main movie class that contains the method for storing the
# contents of each movie
class Movie():
    """ This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    # movie details are listed
    def __init__(self, movie_title, movie_storyline, movie_rated, movie_stars,
                 movie_year, movie_genre, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rated = movie_rated
        self.stars = movie_stars
        self.year = movie_year
        self.genre = movie_genre
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # this function activates the webbrowser to show the trailer
    # for the movie that is defined    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
