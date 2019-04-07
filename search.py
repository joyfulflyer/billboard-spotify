from spotify_auth import auth
from urllib import parse
import json


def search(track_name, artist, type='track'):
    parsed = parse.quote_plus(query)
    query = "artist:{}%20track:{}".format(artist, track_name)
    response = auth.get(
        'https://api.spotify.com/v1/search?q={}&type={}'.format(query, type))
    response_object = json.loads(response.text)
    return response_object
