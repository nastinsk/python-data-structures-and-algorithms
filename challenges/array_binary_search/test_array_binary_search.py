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

def test_original_nums():
  expected = 2
  actual = binary_search([4,8,15,16,23,42], 15)
  assert actual == expected
