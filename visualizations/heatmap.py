import plotly.express as px
import pandas as pd

def generate_listening_heatmap(playback_data):
    playback_data['date'] = pd.to_datetime(playback_data['played_at'])
    playback_data['day'] = playback_data['date'].dt.day_name()
    playback_data['hour'] = playback_data['date'].dt.hour

    heatmap_data = playback_data.pivot_table(index='day', columns='hour', aggfunc='size', fill_value=0)

    fig = px.imshow(heatmap_data, labels=dict(x="Hour", y="Day", color="Listening Frequency"),
                    x=heatmap_data.columns, y=heatmap_data.index, color_continuous_scale='Viridis')
    return fig
