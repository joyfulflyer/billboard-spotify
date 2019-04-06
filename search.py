from spotify_auth import auth


def search(query, type='track'):
    return auth.get('https://api.spotify.com/v1/search?q={}&type={}').format(query, type)
