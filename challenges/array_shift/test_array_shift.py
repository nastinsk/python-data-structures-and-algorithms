from array_shift import insert_shift_array

# "Happy Path" cases
# test should pass for array with number of even element where elements are integers
def test_one():
  expected = [1,2,5,3,4]
  actual = insert_shift_array([1,2,3,4],5)
  assert actual == expected

# test should pass for array with number of even element where elements are letters
def test_two():
  expected = ['a','b','z','c','d']
  actual = insert_shift_array(['a','b','c','d'],'z')                  
  assert actual == expected

# test should pass for array with odd number of elements where elements are letters and integers
def test_three():
  expected = [1,2,3,'a',4,5]
  actual = insert_shift_array([1,2,3,4,5],'a')
  assert actual == expected



# Edge Case
# test should pass for initial array with only 2 elements
def test_four():
  expected = [1,2,1]
  actual = insert_shift_array([1,1],2)
  assert actual == expected



# Expected Failure
# test should pass for initial array with elements ptinted with spaces
def test_five():
  expected = [1,2,9,3]
  actual = insert_shift_array([ 1 ,  2 , 3 ],9)
  assert actual == expected

# test should pass for initial array with only one element
def test_six():
  expected = [1,2]
  actual = insert_shift_array([1],2)
  assert actual == expected


