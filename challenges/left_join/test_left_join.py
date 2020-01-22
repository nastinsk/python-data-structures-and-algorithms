from left_join import left_join
import pytest

@pytest.fixture
def my_dict():
    d1 = {
        'fond':'enamored',
        'wrath':'anger',
        'diligent':'employed',
        'outfit':'garb',
        'guide':'usher'
        }

    return d1

def test_given_example(my_dict):

    d1 = my_dict
    d2 = {
        'fond':'averse',
        'wrath':'delight',
        'diligent':'idle',
        'guide':'follow',
        'flow':'jam'
        }

    assert left_join(d1,d2) == {
                                "fond": ["enamored","averse"],
                                "wrath": ["anger","delight"],
                                "diligent": ["employed","idle"],
                                "outfit": ["garb",None],
                                "guide": ["usher","follow"]
                                }


def test_no_common_keys(my_dict):
    d1 = my_dict
    d2 = {
        'car':'averse',
        'cat':'delight',
        'mouse':'idle',
        'table':'follow',
        'house':'jam'
        }

    assert left_join(d1,d2) == {
                                "fond": ["enamored", None],
                                "wrath": ["anger",None],
                                "diligent": ["employed",None],
                                "outfit": ["garb",None],
                                "guide": ["usher",None]
                                }


def test_different_case():
    d1 = {
        "cat":"a",
        "dog":"b",
        "Cat":"c"
    }

    d2 = {
        "cat":"100",
        "chair":"200",
        "Cat":"300"
    }

    assert left_join(d1,d2) == {
                                "cat": ["a", "100"],
                                "dog": ["b",None],
                                "Cat": ["c", "300"]
                                }


def test_1st_dict_is_empty():
    d1 = {

    }

    d2 = {
        "cat":"100",
        "chair":"200",
        "Cat":"300"
    }

    assert left_join(d1,d2) == {}

def test_2nd_dict_is_empty():
    d1 = {
        "cat":"100",
        "chair":"200",
        "Cat":"300"
    }

    d2 = {}

    assert left_join(d1,d2) == {
                                "cat":["100",None],
                                "chair":["200",None],
                                "Cat":["300", None]
                                }
