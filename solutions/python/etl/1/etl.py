"""
Change the data format of letters and their point values in the game.
"""
def transform(legacy_data):
    """
    param legacy_data: dict
    return dict
    """
    return {letter.lower(): val for val, letters in legacy_data.items() for letter in letters}