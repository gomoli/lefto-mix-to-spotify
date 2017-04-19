from os.path import join, dirname
from os import environ
from dotenv import load_dotenv

def load_env_variables():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    SPOTIPY_CLIENT_ID = environ.get("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = environ.get("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URI = environ.get("SPOTIPY_REDIRECT_URI")
