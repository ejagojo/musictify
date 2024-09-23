import streamlit as st
from spotify_api import get_top_tracks, get_top_artists, get_user_profile, get_recently_played, get_audio_features_for_tracks
from data_processing import process_top_tracks, process_top_artists, process_recently_played
from visualizations.timeline import plot_music_timeline
from visualizations.heatmap import generate_listening_heatmap
from visualizations.genre_map import collaborative_genre_map
from components.music_personality import music_personality_test
from components.nostalgia import nostalgic_throwback
from components.dynamic_background import dynamic_background
from components.carousel import render_carousel

# Authenticate and get user data
st.title('Music Journey Map')
user_profile = get_user_profile()
st.write(f"Hello, {user_profile['display_name']}")

# Map user-friendly labels to Spotify API terms
time_range_map = {
    "Last 1 Month": "short_term",
    "Last 6 Months": "medium_term",
    "All Time (Long Term)": "long_term"
}

# Update selectbox with user-friendly labels
time_range_label = st.selectbox('Select Time Range', list(time_range_map.keys()))

# Use the mapped value for the API call
time_range = time_range_map[time_range_label]

# Fetch top tracks and top artists based on selected time range
top_tracks_data = get_top_tracks(time_range=time_range)
top_artists_data = get_top_artists(time_range=time_range)


# Process data
tracks_df = process_top_tracks(top_tracks_data)
artists_df = process_top_artists(top_artists_data)

# Fetch track IDs to get audio features
track_ids = [item['id'] for item in top_tracks_data['items']]  # List of track IDs
audio_features = get_audio_features_for_tracks(track_ids)  # Fetch audio features for top tracks

# Prepare data for the tracks carousel
track_data = tracks_df.rename(columns={'album_image_url': 'image_url', 'track_name': 'name', 'artist': 'subtitle'}).to_dict('records')

# Prepare data for the artists carousel
artist_data = artists_df.rename(columns={'artist_image_url': 'image_url', 'artist_name': 'name', 'genres': 'subtitle'}).to_dict('records')

# Render the carousel for tracks
st.write("Your Top Tracks")
render_carousel(track_data, "Your Top Tracks")

# Render the carousel for artists
st.write("Your Top Artists")
render_carousel(artist_data, "Your Top Artists")

# Music Personality Test with Audio Features
st.write("Your Music Personality")
personality = music_personality_test(tracks_df['track_name'].tolist(), artists_df['genres'].tolist(), audio_features)
st.write(f"Personality: {personality['personality']}")
st.write(f"Description: {personality['description']}")

# Music Evolution Timeline (based on tracks)
st.write("Music Evolution Timeline")
timeline_fig = plot_music_timeline(tracks_df, category='track_name')
st.plotly_chart(timeline_fig)

# Listening Heatmap
st.write("Your Listening Activity")
recently_played_data = get_recently_played()
if 'items' in recently_played_data:
    recently_played_df = process_recently_played(recently_played_data)
    heatmap_fig = generate_listening_heatmap(recently_played_df)
    st.plotly_chart(heatmap_fig)
else:
    st.write("No playback history available.")

# Collaborative Genre Map (Demo: using mock friend's data)
st.write("Collaborative Genre Map")
friend_genres = ['Pop', 'Rock', 'Jazz']  # Mock data for friends' genres
if 'genres' in artists_df.columns:
    genre_map_fig = collaborative_genre_map(artists_df['genres'].tolist(), friend_genres)
    st.plotly_chart(genre_map_fig)
else:
    st.write("No genres data available.")

# Nostalgic Throwback (Select Year)
year = st.slider("Select a Year for Nostalgia", min_value=2000, max_value=2023, step=1, key="nostalgia_slider_1")
if 'played_at' in recently_played_df.columns:  # Ensure the 'played_at' column exists
    nostalgia_fig = nostalgic_throwback(recently_played_df, year)
    if nostalgia_fig:  # Only plot if the figure is successfully generated
        st.plotly_chart(nostalgia_fig)
else:
    st.write("No 'played_at' data available for nostalgia.")


# Dynamic Background
top_genre = artists_df['genres'].iloc[0] if not artists_df.empty else 'default'
background_class = dynamic_background(top_genre)
st.write(f"Background class for top genre: {background_class}")
