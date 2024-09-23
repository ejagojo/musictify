def dynamic_background(top_genre):
    if top_genre == 'Chill':
        return 'chill-background'
    elif top_genre == 'Rock':
        return 'rock-background'
    else:
        return 'default-background'
