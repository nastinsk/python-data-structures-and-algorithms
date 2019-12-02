user_array=list(input().split(","))
result = []

def reverse(list):
  for i in range(len(list)):
    result.insert(0, list.pop(0))
  print(result)

reverse(user_array)