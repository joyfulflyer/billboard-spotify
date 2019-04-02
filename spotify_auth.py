from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from config import Config

auth = get_auth_object()

def get_auth_object():
    client_id = Config.spotify_client_id
    client_secret = Config.spotify_client_secret
    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
#    token = oauth.fetch_token(token_url='https://provider.com/oauth2/token', auth=auth)
    return oauth


