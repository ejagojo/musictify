import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-top-read user-read-recently-played"  # Add user-read-recently-played scope
))

def get_top_tracks(time_range='medium_term', limit=10):
    """
    Fetches the user's top tracks based on the time range and limit.
    Time ranges: 'short_term' (last 4 weeks), 'medium_term' (6 months), 'long_term' (years)
    """
    return sp.current_user_top_tracks(time_range=time_range, limit=limit)

def get_top_artists(time_range='medium_term', limit=10):
    """
    Fetches the user's top artists based on the time range and limit.
    """
    return sp.current_user_top_artists(time_range=time_range, limit=limit)

def get_user_profile():
    """
    Returns the user's profile information (for display on the web app).
    """
    return sp.current_user()

def get_recently_played(limit=50):
    """
    Fetches the user's recently played tracks, which includes 'played_at' timestamps.
    :param limit: Maximum number of tracks to fetch (max 50)
    :return: List of recently played tracks
    """
    return sp.current_user_recently_played(limit=limit)

def get_audio_features_for_tracks(track_ids):
    """
    Fetch audio features for a list of track IDs from the Spotify API.
    
    :param track_ids: List of Spotify track IDs
    :return: A dictionary containing lists of audio features (e.g., energy, danceability, acousticness)
    """
    audio_features = sp.audio_features(track_ids)
    
    features_data = {
        'energy': [],
        'danceability': [],
        'acousticness': []
    }
    
    for feature in audio_features:
        if feature:
            features_data['energy'].append(feature['energy'])
            features_data['danceability'].append(feature['danceability'])
            features_data['acousticness'].append(feature['acousticness'])

    return features_data

