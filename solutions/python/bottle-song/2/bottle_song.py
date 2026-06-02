"""
Recite the lyrics to that popular children's repetitive song: Ten Green Bottles.
"""

NUM_STR = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def get_bottle_str(count, capitalize=False):
    """
    param count: int
    param capitalize: bool
    return formatted str
    """
    
    word = NUM_STR[count]
    if capitalize:
        word = word.capitalize()
    suffix = "s" if count != 1 else ""
    return f"{word} green bottle{suffix}"

def recite(start, take=1):
    """
    param start: int
    param take: int
    return [str]
    """
    verses = []

    for num in range(start, start-take, -1):
        if verses:
            verses.append("")

        verses.extend([
            f"{get_bottle_str(num, True)} hanging on the wall,",
            f"{get_bottle_str(num, True)} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {get_bottle_str(num - 1, False)} hanging on the wall."
        ])

    return verses
