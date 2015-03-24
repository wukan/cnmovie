from __future__ import absolute_import

import requests

from scripts.fetch_movie_info import fetch_movie_info

API_KEY = 'wayxxnw2ppq8g98m57c8wmup'
BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0'

def fetch_tomato_movie_info(tomato_id):
    data = {
        'apikey': API_KEY, 
    } 
    url = '%s/movies/%s.json' % (BASE_URL, tomato_id)
    r = requests.get(url, params=data)
    print 'FETCHING: %s' % r.url

    r.raise_for_status()

    movie = r.json()
    if 'imdb' in movie.get('alternate_ids', {}):
        fetch_movie_info('tt' + movie['alternate_ids']['imdb'])

def fetch_showtime(page=1, limit=16):
    data = {
        'apikey': API_KEY,
        'page_limit': limit,
        'page': page,
    }
    url = '%s/lists/movies/in_theaters.json' % BASE_URL
    r = requests.get(url, params=data)
    print 'FETCHING: %s' % r.url

    r.raise_for_status()

    resp = r.json()
    movies = resp['movies']
    for movie in movies:
        if 'imdb' in movie.get('alternate_ids', {}):
            fetch_movie_info('tt' + movie['alternate_ids']['imdb'])
    if resp['links'].get('next', None):
        fetch_showtime(page + 1, limit)