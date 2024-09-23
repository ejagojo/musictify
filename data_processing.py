import pandas as pd

def process_top_tracks(data):
    """
    Transforms the top tracks data into a DataFrame for visualization.
    """
    tracks = []
    for item in data['items']:
        track_info = {
            'track_name': item['name'],
            'artist': item['artists'][0]['name'],
            'popularity': item['popularity'],
            'album': item['album']['name'],
            'release_date': item['album']['release_date'],
            'album_image_url': item['album']['images'][0]['url']
        }
        tracks.append(track_info)
    
    return pd.DataFrame(tracks)

def process_top_artists(data):
    """
    Transforms the top artists data into a DataFrame for visualization.
    """
    artists = []
    for item in data['items']:
        artist_info = {
            'artist_name': item['name'],
            # Ensure 'genres' exists; otherwise, set it to an empty list
            'genres': ', '.join(item['genres']) if 'genres' in item and item['genres'] else 'Unknown',
            'popularity': item['popularity'],
            'artist_image_url': item['images'][0]['url'] if item['images'] else None
        }
        artists.append(artist_info)

    return pd.DataFrame(artists)

    

def process_recently_played(data):
    """
    Processes the recently played tracks data to extract relevant fields including played_at timestamps.
    """
    tracks = []
    for item in data['items']:
        track_info = {
            'track_name': item['track']['name'],
            'artist': item['track']['artists'][0]['name'],
            'popularity': item['track']['popularity'],
            'album': item['track']['album']['name'],
            'release_date': item['track']['album']['release_date'],
            'played_at': item['played_at'],  # Make sure this is captured
            'album_image_url': item['track']['album']['images'][0]['url']
        }
        tracks.append(track_info)

    return pd.DataFrame(tracks)


