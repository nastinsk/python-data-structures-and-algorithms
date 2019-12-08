def binary_search(arr, key):
  low = 0
  high = len(arr)
  while len(arr) > 0:
    middle = (low+high) // 2
    if arr[middle] == key:
      return middle
    if arr[middle] < key:
      low= middle
    if arr[middle] > key:
      high= middle
    if middle == 0 or middle == len(arr) - 1:
      return -1
  return -1


# def binary_search(arr, key):
#     while len(arr) > 0:
#         try:
#             middle = len(arr)//2

#             if arr[middle] == key:
#                 return middle
#             if arr[middle] > key:
#                 binary_search( arr[:middle], key)
#             if arr[middle] < key:
#                 binary_search(arr[middle:], key)
#         except IndexError:
#             return -1

#     return -1

