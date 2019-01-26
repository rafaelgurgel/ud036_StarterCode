import fresh_tomatoes as application
import media_controller





all_movies = media_controller.generateMockList()


application.open_movies_page(all_movies)