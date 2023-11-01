from flask import Flask, request, jsonify
import requests

app = Flask(__name)

# SQLite database setup and API endpoints

@app.route('/api/movies', methods=['GET', 'POST', 'DELETE'])
def manage_movies():
    if request.method == 'GET':
        # Handle GET request to fetch and return favorite movies
        # You can query the SQLite database and return the data as JSON

    elif request.method == 'POST':
        # Handle POST request to add a favorite movie to the database
        # Extract movie details from the request and insert them into the database

    elif request.method == 'DELETE':
        # Handle DELETE request to remove a favorite movie from the database
        # Extract the movie ID from the request and delete the record

@app.route('/api/tmdb_movie', methods=['GET'])
def fetch_tmdb_movie():
    # Handle GET request to fetch movie data from The Movie Database (TMDb) API
    tmdb_api_url = 'https://api.themoviedb.org/3/movie/550?api_key=bd74380ad0f3a6bc2db537543036493a'

    try:
        response = requests.get(tmdb_api_url)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Error fetching movie data from TMDb API'})

if __name__ == '__main__':
    app.run(debug=True)
