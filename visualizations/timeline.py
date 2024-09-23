import plotly.express as px

def plot_music_timeline(df, category='track_name'):
    """
    Creates a timeline of music evolution based on the category (e.g., track_name, artist).
    Assumes that the DataFrame contains a 'release_date' column.
    """
    # Ensure the 'release_date' exists in df
    if 'release_date' not in df.columns:
        raise ValueError("DataFrame does not contain 'release_date' column")

    fig = px.line(df, x='release_date', y=category, title=f'Music Journey: {category.capitalize()} Over Time')
    return fig