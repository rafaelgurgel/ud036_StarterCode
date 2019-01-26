#media_controller.py

def generateMockList():
    import media
    movie1 = media.Movie("Transformers - The Last Knight", "The Last Knight returns", "https://m.media-amazon.com/images/M/MV5BMTk3OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_.jpg", "trailer")

    movie2 = media.Movie("name", "storyline", "image", "trailer")
    movie3 = media.Movie("name", "storyline", "image", "trailer")
    return [movie1, movie2, movie3]