import plotly.graph_objs as go

def animated_transition(data_frame, x_col, y_col):
    """
    Adds animated transitions between visualizations.

    :param data_frame: DataFrame with the data to visualize
    :param x_col: Column to use for x-axis
    :param y_col: Column to use for y-axis
    :return: Plotly figure with animation
    """
    fig = go.Figure(data=[go.Scatter(x=data_frame[x_col], y=data_frame[y_col], mode="markers")])

    fig.update_layout(
        updatemenus=[dict(type="buttons", showactive=False,
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None, dict(frame=dict(duration=500, redraw=True))])])])

    frames = [go.Frame(data=[go.Scatter(x=data_frame[data_frame.index <= k][x_col],
                                        y=data_frame[data_frame.index <= k][y_col])]) for k in range(1, len(data_frame))]
    
    fig.frames = frames
    return fig
