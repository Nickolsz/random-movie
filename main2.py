from Letterboxd import *
import sys
from movie_help import *
from IMDB import *

if '-help' in sys.argv:
    printhelp()


if '-l' in sys.argv:
    username_idx = sys.argv.index('-l')+1
    username = sys.argv[username_idx]
    amount_idx = sys.argv.index('-n')+1
    amount = int(sys.argv[amount_idx])
    if not '-g' in sys.argv:
        get_movie_no_genre(username,amount)
    else:
       genre_idx = sys.argv.index('-g')+1
       genre = sys.argv[genre_idx]
       get_movie_with_genre(username,genre,amount)



if '-i' in sys.argv:
    amount_idx = sys.argv.index('-n')+1
    amount = int(sys.argv[amount_idx])
    if not '-g' in sys.argv:
        getMovies_IMDB(amount)
    else:
        genre_idx = sys.argv.index('-g')+1
        genre = sys.argv[genre_idx]
        getMovies_IMDB_Genre(genre, amount)