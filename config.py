import base64
from os import environ


class Config:
    db_username = environ.get('DB_USERNAME')
    db_password = environ.get('PASS')
    db_host = environ.get('HOST')
    db_name = environ.get('DATABASE')
    spotify_client_id = environ.get('SPOTIFY_CLIENT',
                                    '57414f39fbe74b489c4118158fbec637')
    spotify_client_secret = environ.get('SPOTIFY_SECRET')

    def get_encoded_header_content(self):
        return base64.b64encode('b{}:{}'.format(
            spotify_client_id, spotify_client_secret))

