from repeated_word import find_first_repeat
import pytest

def test_regular_str():
    text = "Once upon a time, there was a brave princess who..."
    assert find_first_repeat(text) == "a"

def test_bigger_different_case():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert find_first_repeat(text) == "it"

def test_no_tepeat():
    text = "a b c, d."
    assert find_first_repeat(text) == None

def test_punktuation_case():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert find_first_repeat(text) == 'summer'

def test_numbers_input():
    text = 135
    with pytest.raises(TypeError):
        result = find_first_repeat(text)

def test_repeat_in_the_end():
    text = "red blue yellow green green blue blue"
    assert find_first_repeat(text) == "green"

def test_list_input():
    text = ['a', 'f', 'a', 'vf']
    with pytest.raises(TypeError):
        result = find_first_repeat(text)


