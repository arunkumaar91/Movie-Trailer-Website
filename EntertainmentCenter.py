import fresh_tomatoes
import media

""" This script creates several instances for the class movie """

pursuit_of_happyness = media.Movie("Pursuit of Happyness",
                                   "A Father overcomes the struggle of his life along with his son.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg", # NOQA
                                   "https://www.youtube.com/watch?v=00uTFVnWJMw")

forrest_gump = media.Movie("Forrest Gump",
                           "A man inspires people with child-like optimism.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

karate_kid = media.Movie("The Karate Kid",
                         "A young boy learn Kung fu to fight against his enemy.",
                         "http://images4.fanpop.com/image/photos/19500000/The-Kararte-Kid-the-karate-kid-2010-19510496-1280-1024.jpg", # NOQA
                         "https://www.youtube.com/watch?v=2SmmxvHLsKk")

interstellar = media.Movie("Interstellar",
                           "A physicist vision to save the earth population.",
                           "http://www.fatmovieguy.com/wp-content/uploads/2014/07/Interstellar-Movie-Poster-2.jpg", # NOQA
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

the_martian = media.Movie("The Martian",
                          "A stranded visitor to mars mission survive for his life in mars.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")
                          
the_dark_night = media.Movie("The Dark Night",
                             "Batman trying to keep a tight lid on crime in Gotham City", 
                             "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", # NOQA
                             "https://www.youtube.com/watch?v=kmJLuwP3MbY")

# movies variable stores the array of movie objects
movies = [
    pursuit_of_happyness, forrest_gump, karate_kid,
    interstellar, the_martian, the_dark_night
    ]

""" open_movies_page function creates
and opens the output file in web browser
"""
fresh_tomatoes.open_movies_page(movies)
