import media
import fresh_tomatoes

"""Create movie objects using instances from the Movie class.
Args:
    Title: Movie title
    Image: Movie poster image link
    Trailer: Youtube trailer link
"""
toy_story = media.Movie("Toy story 3",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=yUmSVcttXnI")

alien_Covenant = media.Movie("Alien Covenant",
                             "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                             "https://www.youtube.com/watch?v=svnAD0TApb8")

i_robot = media.Movie("I, Robot",
                      "https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg",
                      "https://www.youtube.com/watch?v=rL6RRIOZyCM")

minority_report = media.Movie("Minority Report",
                              "https://upload.wikimedia.org/wikipedia/en/4/44/Minority_Report_Poster.jpg",
                              "https://www.youtube.com/watch?v=aGWQYgZZEEQ")

equilibrium = media.Movie("Equilibrium",
                          "https://upload.wikimedia.org/wikipedia/en/f/f6/Equilibriumposter.jpg",
                          "https://www.youtube.com/watch?v=raleKODYeg0")

"""Create list of movie objects."""
movies = [toy_story, edge_of_tomorrow, alien_Covenant, i_robot, minority_report, equilibrium]

"""Pass list of movies to supplied fresh_tomatoes file to display in web browser."""
fresh_tomatoes.open_movies_page(movies)
