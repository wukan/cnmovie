from __future__ import absolute_import

from datetime import datetime

import requests

from scripts.fetch_showtimes import fetch_tomato_movie_info
from scripts.fetch_movie_info import fetch_movie_info

BASE_URL = 'https://api.flixster.com/api/v1/ticketing/theaters'

def fetch_theaters(postal='94122', limit=16):
    data = {
        'showtimes': True,
        'postal': postal,
        'fullMovieInfo': True,
        'date': datetime.now().strftime('%Y%m%d'),
        'limit': limit,
    }
    r = requests.get(BASE_URL, params=data)
    print 'FETCHING: %s' % r.url

    r.raise_for_status()

    resp = r.json()
    theaters = resp.get('theaters', [])
    movie_ids = set()
    for theater in theaters:
    	for movie in theater.get('movies', []):
    		if 'id' in movie:
    			movie_ids.add(movie['id'])
    for movie_id in movie_ids:
    	fetch_tomato_movie_info(movie_id)
