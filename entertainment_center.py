import fresh_tomatoes
import media

# the database containing all favorite movie information
school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of a rock band, Dewey"
                             " Finn becomes a substitute teacher of a strict"
                             " elementary private school, only to try and turn"
                             " it into a rock band.",
                             "PG-13",
                             "Jack Black, Mike White, Joan Cusack",
                             "2003",
                             "Comedy, Family, Music",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
                             
tombstone = media.Movie("Tombstone",
                        "A successful lawman's plans to retire anonymously"
                        " in Tombstone, Arizona, are disrupted by the kind"
                        " of outlaws he was famous for eliminating.",
                        "R",
                        "Kurt Russell, Val Kilmer, Sam Elliott, Bill Paxton",
                        "1993",
                        "Action, Biography, Drama",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/Tombstoneposter.jpeg",  # NOQA
                        "https://www.youtube.com/watch?v=XTWYKf5hXIg")

smokey_and_the_bandit = media.Movie("Smokey and the Bandit",
                                    "The Bandit (Burt Reynolds) is hired on to"
                                    " run a tractor trailer full of beer over"
                                    " county lines in hot pursuit by a pesky"
                                    " sheriff.",
                                    "PG",
                                    "Burt Reynolds, Sally Field, Jerry Reed,"
                                    " Jackie Gleason",
                                    "1977",
                                    "Action, Comedy",
                                    "https://upload.wikimedia.org/wikipedia/en/c/cb/Smokey_And_The_Bandit_Poster.jpg",  # NOQA
                                    "https://www.youtube.com/watch?v=IzMpOvKxXdM")  # NOQA


the_blues_brothers = media.Movie("The Blues Brothers",
                                 "Jake Blues, just out from prison,"
                                 " puts together his old band to save the"
                                 " Catholic home where he and brother"
                                 " Elwood were raised.",
                                 "R",
                                 "John Belushi, Dan Aykroyd, Cab Calloway",
                                 "1980",
                                 "Action, Comedy, Crime",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMzdhOTJmYmQtMmE0OS00ZDMyLWFkZDItZmZmMGJlNGUyNjNhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX668_AL_.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=_CYMYYHHe90")

the_italian_job = media.Movie("The Italian Job",
                              "After being betrayed and left for dead in"
                              " Italy, Charlie Croker and his team plan an"
                              " elaborate gold heist against their"
                              " former ally.",
                              "PG-13",
                              "Donald Sutherland, Mark Wahlberg,"
                              " Edward Norton",
                              "2003",
                              "Action, Crime, Thriller",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BNDYyNzYxNjYtNmYzMC00MTE0LWIwMmYtNTAyZDBjYTIxMTRhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=5Eyw-Qiwpj0")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels"
                         " about the true nature of his reality and his"
                         " role in the war against its controllers.",
                         "R",
                         "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                         "1999",
                         "Action, Sci-Fi",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWMxOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,723,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

# all movies to be included in the dispalyed page should be listed below
movies = [school_of_rock, tombstone, smokey_and_the_bandit,
          the_blues_brothers, the_italian_job, the_matrix]

# The below command creates an instance for each movie in the
# open_movies_page function which is defined in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)

