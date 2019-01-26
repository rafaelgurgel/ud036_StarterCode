#media_controller.py

def generateMockList():
    import media
    movie1 = media.Movie("Transformers - The Last Knight",
                        "2017",
                        "Autobots and Decepticons are at war, with humans on the sidelines. Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth. ",
                        "https://m.media-amazon.com/images/M/MV5BMTk3OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_.jpg",
                        "https://youtu.be/AntcyqJ6brc" ,
                        "Sci-Fi, Fantasy, Action")

    movie2 = media.Movie("The Dark Knight Rises", 
                        "2012",
                        " Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane. ",
                        "https://m.media-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_.jpgimage",
                         "https://youtu.be/GokKUqLcvD8",
                         "Adventure, Fantasy, Action")

    movie3 = media.Movie("The Dark Knight",
                        "2008",
                        "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice. ",
                        "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                         "https://youtu.be/EXeTwQWrcwY",
                         "Adventure, Fantasy, Action")
    return [movie1, movie2, movie3]