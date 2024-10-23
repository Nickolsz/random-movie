from bs4 import BeautifulSoup 
import requests
import random



def get_page_count(url):
    response = requests.get(url) #sends request to get the URL we want
    soup = BeautifulSoup(response.content, 'html.parser') #creates BS object, which is therefore the HTML content of our page
    
    pagination = soup.find('div', {'class': 'pagination'}) # line of pages on the bottom of website
    #Error case If there is no pagination then we know the users watchlist is not long enough for multiple pages and is therefore only one
    if pagination: #if theres multiple pages
        li_elements = pagination.find_all('li')
        last_page_text = li_elements[-1].get_text() # Get the last 'li' element and retrieve its text
        return int(last_page_text) # Convert the text to an integer and return it
    else:
        return 1


def get_movies(url):
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, 'html.parser')
    
    movie_titles = []
    movie_list = soup.find('ul', {'class': 'poster-list -p125 -grid -scaled128'}) # Locate the movie list element
    if movie_list:
        image_elements = movie_list.find_all('img', alt=True)  # Extract the 'alt' attribute from each 'img' element
        for img in image_elements: # Create a list of all possible movies
            movie_titles.extend([img['alt']]) 
    else:
        print(f"No movies found at URL: {url}")  # Handle the case where no movie list is found
    return movie_titles


def get_movie_no_genre(username, amount):
    url_pagination = f'https://letterboxd.com/{username}/watchlist'
    movie_titles = []
    random_movies =[]
    for i in range(1, get_page_count(url_pagination) + 1): #use the amount of pages we found to iterate through all movies, on all pages and compule a list.
        url = f'https://letterboxd.com/{username}/watchlist/page/{i}/'
        movie_titles.extend(get_movies(url))
    for j in range(amount):
        movie = random.choice(movie_titles)
        random_movies.append(movie)
    print(random_movies)
    return random_movies

def get_movie_with_genre(username, genre, amount):
    movie_titles = []
    random_movies = []

    # Check if genre is provided; if not, default to the user's entire watchlist
    if genre and genre.lower() != "none":
        url_pagination = f'https://letterboxd.com/{username}/watchlist/genre/{genre}'
        for i in range(1, get_page_count(url_pagination) + 1):
            url = f'https://letterboxd.com/{username}/watchlist/genre/{genre}/page/{i}/'
            movie_titles.extend(get_movies(url))
    else:
        # No genre provided, so get movies from the entire watchlist
        url_pagination = f'https://letterboxd.com/{username}/watchlist'
        for i in range(1, get_page_count(url_pagination) + 1):
            url = f'https://letterboxd.com/{username}/watchlist/page/{i}/'
            movie_titles.extend(get_movies(url))
    
    # If there are fewer movies than the requested amount, notify the user
    if len(movie_titles) < amount:
        print(f"Note: Only {len(movie_titles)} movies available for your selection")
    else:
        for j in range(amount):
            movie = random.choice(movie_titles)
            random_movies.append(movie)
    
    print(random_movies)
    return random_movies

if __name__ == '__main__':
    get_movie_no_genre('nolsz', 2)
