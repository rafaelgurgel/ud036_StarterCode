class Movie():

    def __init__(self, title, storyLine, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyLine = storyLine
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    def show_youtube_trailer():
        webbrowser.open(self.url)
