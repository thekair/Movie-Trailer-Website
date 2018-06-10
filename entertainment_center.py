import fresh_tomatoes
import media

# create an instance form class movie -- the movie gladiator
gladiator = media.Movie("Gladiator", "A slave who defited the emperor of Rome",
                        "https://upload.wikimedia.org/wikipedia"
                        "/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=uvbavW31adA")

# create an instance form class movie -- the movie breaveheart
braveheart = media.Movie("Braveheart",
                         "William Wallace is the medieval Scottish patriot"
                         " who is spurred into revolt against the English"
                         " when the love of his life is slaughtered",
                         "https://upload.wikimedia.org/wikipedia"
                         "/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=1NJO0jxBtMo")

# create an instance form class movie -- the movie shawshank redemption
shawshank_redemption = media.Movie("Shawshank redemption",
                                   "the story of banker Andy Dufresne"
                                   " (Tim Robbins), who is sentenced to life"
                                   " in Shawshank State Penitentiary for the "
                                   " murder of his wife and her lover, despite"
                                   " his claims of innocence",
                                   "https://upload.wikimedia.org/wikipedia/en"
                                   "/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=6hB3S9bIaco")

# add all movie objects to a list so that we can pass it to the next function
movies = [gladiator, braveheart, shawshank_redemption]

# call function open_movies_page()
# which will take in the list movies
# and generate an HTML file including this content,
# producing a website to showcase the movies.
fresh_tomatoes.open_movies_page(movies)
