---
toc: true
comments: false
layout: post
title: Movie Api Copy
description: Find the Perfect Movie
type: plans
courses: { compsci: {week: 0} }
---
<script>
import requests
from bs4 import BeautifulSoup

def fetch_movie_list():
    url = "https://en.wikipedia.org/wiki/Lists_of_films"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract film information from the page
    film_list = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and "/wiki/" in href and "List_of" in href:
            film_list.append(link.text)
    
    return film_list

def is_movie_length_within_range(movie_length, min_length, max_length):
    # Helper function to check if movie length is within the specified range
    if movie_length.endswith('min'):
        movie_length = movie_length.replace('min', '').strip()
        try:
            movie_length_in_minutes = int(movie_length)
            return min_length <= movie_length_in_minutes <= max_length
        except ValueError:
            return False
    return False

def filter_movies_by_criteria(movies, lead_actor, genre, year, min_length, max_length):
    filtered_movies = []
    for movie in movies:
        # Add your filtering logic here based on lead_actor, genre, year, and length
        # For simplicity, let's just include the movie if any of the criteria matches
        if (lead_actor in movie or 
            genre in movie or 
            year in movie):
            # Check if the movie length is within the specified range
            movie_length = movie.split(" ")[-1]  # Extracting the movie length from the end of the movie title
            if is_movie_length_within_range(movie_length, min_length, max_length):
                filtered_movies.append(movie)
    
    return filtered_movies

if __name__ == "__main__":
    # Input parameters
    lead_actor = input("Enter lead actor: ")
    genre = input("Enter genre: ")
    year = input("Enter year: ")
    desired_length = int(input("Enter desired movie length (in minutes): "))
    
    # Calculate the min and max lengths based on the desired length
    min_length = max(0, desired_length - 15)  # Minimum length can't be negative
    max_length = desired_length + 15  # Maximum length
    
    # Fetch the list of movies from Wikipedia
    movie_list = fetch_movie_list()
    
    if movie_list:
        # Filter movies based on the provided criteria and movie length range
        filtered_movies = filter_movies_by_criteria(movie_list, lead_actor, genre, year, min_length, max_length)
        
        # Display the filtered movies
        print("Filtered movies:")
        for movie in filtered_movies:
            print(movie)
    else:
        print("Failed to fetch the movie list.")
</script>