from two_sum import two_sum

def test_initial_case():
   assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_empty_lst():
    assert two_sum([], 9) == []

def test_one_el_in_lst():
    assert two_sum([1], 9) == []

def test_one_el_in_lst():
    assert two_sum([1,1,1,1], 2) == [0,1]
