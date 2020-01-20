import re

def find_first_repeat(text):
    """Function to find the first repeated word in a text."""
    
    if not isinstance(text, str):
        raise TypeError

    word_set = set()
    word_list = re.findall(r'[A-Za-z]+', text.lower())

    for word in word_list:
        if word in word_set:
            return word
        word_set.add(word)
    return None

