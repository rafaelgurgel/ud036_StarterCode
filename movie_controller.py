


class MovieController():

    def generateMockList(self):
        import media
        movie1 = media.Movie("name", "storyline", "image", "trailer")
        movie2 = media.Movie("name", "storyline", "image", "trailer")
        movie3 = media.Movie("name", "storyline", "image", "trailer")
        return [movie1, movie2, movie3]
        
