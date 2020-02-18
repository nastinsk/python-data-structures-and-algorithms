def two_sum(lst, target):

    nums_dict = {}
    results_arr = []
    for i, el in enumerate(lst):
        nums_dict[el] = i

    for i in range(len(lst)):
        results_arr[0] = i
        second_val = target - lst[i]
        if second_val in nums_dict:
            results_arr[1] = nums_dict[second_val]

    return results_arr
