import requests
from bs4 import BeautifulSoup
import random

# Function to get movies without genre
def getMovies_IMDB(amount):
    movie_titles = []
    random_movies = []
    
    # URL containing all 500 movies
    url = 'https://www.imdb.com/list/ls058366250/?sort=list_order,asc&st_dt=&mode=detail'
    
    # Adding headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all movie titles based on the new structure
    movie_elements = soup.find_all('h3', class_='ipc-title__text')

    for movie_element in movie_elements:
        movie_title = movie_element.get_text(strip=True)
        
        # Remove the number from the movie title
        movie_title = movie_title.split('. ', 1)[-1]
        movie_titles.append(movie_title)
    
    # Select the requested amount of random movies
    for _ in range(amount):
        movie = random.choice(movie_titles)
        random_movies.append(movie)

    print(random_movies)
    return random_movies


# Function to get movies with a specific genre
def getMovies_IMDB_Genre(genre, amount):
    movie_titles = []
    random_movies = []
    
    # Adjust the URL with the genre parameter, but still only one page
    url = f'https://www.imdb.com/list/ls058366250/?sort=list_order%2Casc&genres={genre}'
    
    # Adding headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all movie titles based on the new structure
    movie_elements = soup.find_all('h3', class_='ipc-title__text')

    for movie_element in movie_elements:
        movie_title = movie_element.get_text(strip=True)
        
        # Remove the number from the movie title
        movie_title = movie_title.split('. ', 1)[-1]
        movie_titles.append(movie_title)
    
    # Select the requested amount of random movies
    for _ in range(amount):
        movie = random.choice(movie_titles)
        random_movies.append(movie)

    print(random_movies)
    return random_movies

if __name__ == '__main__':
    # Example for genre
    getMovies_IMDB_Genre('Drama', 2)

    # Example without genre
    getMovies_IMDB(2)
