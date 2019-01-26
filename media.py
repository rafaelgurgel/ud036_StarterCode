class Movie():

    def __init__(self, title, year, storyLine, poster_image_url, trailer_youtube_url, genre):
        self.title = title
        self.year = year
        self.storyLine = storyLine
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.genre = genre
    
    def show_youtube_trailer():
        webbrowser.open(self.url)
