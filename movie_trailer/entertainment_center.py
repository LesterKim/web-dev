import fresh_tomatoes
import media

# Create Movie instances from media.py with title, description, poster, and video
blazing_saddles = media.Movie('Blazing Saddles',
                      'A black sheriff comes to town',
                      'https://upload.wikimedia.org/wikipedia/en/7/7b/Blazing_saddles_movie_poster.jpg',
                      'https://www.youtube.com/watch?v=VKayG1TrfuE')

talladega_nights = media.Movie('Tallagdega Nights',
                      'An idiot racecar champion',
                      'https://upload.wikimedia.org/wikipedia/en/e/e7/Talladega_nights.jpg',
                      'https://www.youtube.com/watch?v=-zPcMma_C7A')

eyes_wide_shut = media.Movie('Eyes Wide Shut',
                      'Tom Cruise infiltrates a sex cult',
                      'https://upload.wikimedia.org/wikipedia/en/8/87/Eyes_Wide_Shut_poster.jpg',
                      'https://www.youtube.com/watch?v=YEfyfcEdW4Y')

enter_the_dragon = media.Movie('Enter The Dragon',
                      'Bruce Lee fights a guy with a claw',
                      'https://upload.wikimedia.org/wikipedia/en/e/ef/Enter_the_dragon.jpg',
                      'https://www.youtube.com/watch?v=81jCPIag4KA')

# Set up as array to feed into next function
movies = [blazing_saddles, talladega_nights, eyes_wide_shut, enter_the_dragon]

# Insert movie data into HTML
fresh_tomatoes.open_movies_page(movies)