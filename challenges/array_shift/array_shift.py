def insert_shift_array(l,b):
  middle = len(l) // 2
  if len(l) % 2 == 0:

    return l[:middle] + [b] + l[middle:]
  else:
    return l[:middle + 1] + [b] + l[middle +1:]
