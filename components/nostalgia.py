import pandas as pd
import plotly.express as px
import streamlit as st

def nostalgic_throwback(tracks_df, year):
    """
    Filters and displays the user's top tracks from a given year in a timeline format.
    
    :param tracks_df: DataFrame containing the user's recently played tracks.
    :param year: Year for which to filter tracks.
    :return: Plotly timeline visualization of top tracks for the selected year.
    """

    # Ensure the 'played_at' column is present and in datetime format
    if 'played_at' not in tracks_df.columns:
        st.error("The 'played_at' column is missing from the data.")
        return None

    # Convert 'played_at' to datetime if it's not already
    try:
        tracks_df['played_at'] = pd.to_datetime(tracks_df['played_at'])
    except Exception as e:
        st.error(f"Error converting 'played_at' to datetime: {e}")
        return None

    # Extract the year from the 'played_at' column
    tracks_df['year'] = tracks_df['played_at'].dt.year

    # Filter tracks from the selected year
    tracks_from_year = tracks_df[tracks_df['year'] == year]

    if tracks_from_year.empty:
        st.warning(f"No tracks found for the year {year}.")
        return None

    # Create a timeline plot using Plotly Express
    fig = px.timeline(
        tracks_from_year, 
        x_start='played_at', 
        x_end='played_at', 
        y='track_name',
        title=f"Your Top Tracks from {year}",
        labels={'track_name': 'Track'}
    )

    return fig
