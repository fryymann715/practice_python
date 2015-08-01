__author__ = 'ideans'
import webbrowser

class Video():

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print("Video Title: " + self.title)
        print("Video Length: " + str(self.duration))

class Movie(Video):

    def __init__(self, title, duration, storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
        print("Movie Title:" + self.title)
        print("Movie Length: " + str(self.duration))
        print("Trailer URL: " + self.trailer_youtube_url)

class Tvshow(Video):

    def __init__(self, title, duration, storyline, number_of_seasons):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.number_of_seasons = number_of_seasons

    def show_info(self):
        print("Show Title: "+ self.title )
        print("Episode Length: " + str(self.duration))
        print("Number of Seasons: " + str(self.number_of_seasons))