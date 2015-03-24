from __future__ import absolute_import

import requests

BASE_URL = 'http://www.omdbapi.com/'

def fetch_movie_info(imdb_id):
    data = {
        'i': imdb_id,
        'plot': 'short',
        'r': 'json',
    }
    url = '%s/' % BASE_URL
    r = requests.get(url, params=data)
    print 'FETCHING: %s' % r.url

    r.raise_for_status()

    movie = r.json()
    if is_cn_movie(movie):
        print '##########################'
    print 'Title: %s\nCountry: %s\nLanguage: %s' % (movie.get('Title', ''), movie.get('Country', ''), movie.get('Language', ''))
    if is_cn_movie(movie):
        print '##########################'

def is_cn_movie(movie):
    countries = movie.get('Country', '')
    if 'China' in countries or 'Taiwan' in countries or 'Hong Kong' in countries:
        return True
    languages = movie.get('Language', '')
    if 'Chinese' in languages or 'Mandarin' in languages or 'Cantonese' in languages:
        return True
    return False