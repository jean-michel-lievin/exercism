"""
Given a list of inputs, generate the relevant proverb. 
"""
def proverb(*input_data, qualifier=None, first_word=None):
    """
    param input_data (str)
    param: qualifier (str)
    param: first_word (str)
    return [str]
    """
    if not input_data:
        return []

    if first_word is None:
        first_word, *words = input_data

    if len(input_data) == 1:
        last_word = f"{qualifier} {first_word}" if qualifier else first_word
        return [f"And all for the want of a {last_word}."]

    current, second, *rest = input_data
    current_line = f"For want of a {current} the {second} was lost." 
    return [current_line] + proverb(second, *rest, qualifier=qualifier, first_word=first_word)








    











        

    # if first_word is None:
    #     [first_word, *_] = input_data

    # if len(input_data) == 1:
    #     # On combine proprement le qualifier et le premier mot mémorisé
    #     final_item = f"{qualifier} {first_word}" if qualifier else first_word
    #     return [f"And all for the want of a {final_item}."]

    # Unpacking pour consommer la paire actuelle
    # current, second, *rest = input_data
    # current_line = f"For want of a {current} the {second} was lost."

    # On lance la machine avec nos données de départ
    # return [current_line] + proverb(second, *rest, qualifier=qualifier, first_word=first_word)