
def merge_sort(lst):

    """function to prvide a merge sort on the given list, calles recursively """
    n = len(lst)

    if n > 1:
        mid = n//2
        left = lst[: mid]
        right = lst[mid:]

        # sort the left side
        merge_sort(left)

        # sort the right side
        merge_sort(right)


        # merge the sorted left and right sides together
        merge(left, right, lst)

def merge(left, right, lst):
    """function to merge left sublist  and rightsublist to the list in proper order"""

    i = 0
    j = 0
    k = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        for el in right[j:]:
            lst[k] = el
            k += 1

    else:
        for el in left[i:]:
            lst[k] = el
            k +=1

