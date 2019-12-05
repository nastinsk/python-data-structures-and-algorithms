from array_binary_search import binary_search

# "Happy Path" cases

def test_simple():
  expected = 3
  actual = binary_search([1,2,3,4,5,6],4)
  assert actual == expected

def test_original_nums():
  expected = 2
  actual = binary_search([4,8,15,16,23,42], 15)
  assert actual == expected

def test_absence():
  expected = -1
  actual = binary_search([11,22,33,44,55,66,77], 90)
  assert actual == expected

# Expected Failure
def test_num_in_left():
  expected = 0
  actual = binary_search([11,22,33,44,55,66,77,89,100], 11)
  assert actual == expected

def test_num_in_right():
  expected = 8
  actual = binary_search([11,22,33,44,55,66,77,89,100], 100)
  assert actual == expected

def test_num_in_middle():
  expected = 4
  actual = binary_search([11,22,33,44,55,66,77,89,100], 55)
  assert actual == expected

def test_num_not_in_right():
  expected = -1
  actual = binary_search([11,22,33,44,55,66,77,89,100], 101)
  assert actual == expected

def test_num_not_in_left():
  expected = -1
  actual = binary_search([11,22,33,44,55,66,77,89,100], 10)
  assert actual == expected

# Edge Cases
def test_two_element_arr():
  expected = 1
  actual = binary_search([10, 34], 34)
  assert actual == expected

def test_two_element_arr_anbsence():
  expected = -1
  actual = binary_search([10, 34], 19)
  assert actual == expected

def test_empty_array():
  expected = -1
  actual = binary_search([], 19)
  assert actual == expected

def test_empty_array_negative():
  expected = -1
  actual = binary_search([], -1)
  assert actual == expected
