def two_sum(lst, target):

    nums_dict = {}
    results_arr = []

    for i, el in enumerate(lst):

        if el in nums_dict and nums_dict[el][1] < 2:
            nums_dict[el]= (i, 2)

        if el not in nums_dict:
            nums_dict[el] = (i, 1)



    for i in range(len(lst)):

        second_val = target - lst[i]

        if second_val in nums_dict:

            results_arr.append(i)


            results_arr.append(nums_dict[second_val][0])

            return results_arr

    return results_arr

