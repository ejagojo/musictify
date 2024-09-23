import plotly.graph_objs as go

def collaborative_genre_map(user_genres, friend_genres):
    shared_genres = set(user_genres).intersection(friend_genres)
    unique_user_genres = set(user_genres).difference(friend_genres)
    unique_friend_genres = set(friend_genres).difference(user_genres)

    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=[len(shared_genres)] * len(shared_genres),
        theta=list(shared_genres),
        fill='toself',
        name='Shared Genres'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[len(unique_user_genres)] * len(unique_user_genres),
        theta=list(unique_user_genres),
        fill='toself',
        name='Your Unique Genres'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[len(unique_friend_genres)] * len(unique_friend_genres),
        theta=list(unique_friend_genres),
        fill='toself',
        name="Friend's Unique Genres"
    ))

    return fig
