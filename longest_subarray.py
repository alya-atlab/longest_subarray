def longest_subarray(array):
    zeros_count = 0
    ones_count = 0
    for i in array:
        if i == 0:
            zeros_count += 1
        else:
            ones_count += 1
    if (
        zeros_count <= ones_count
    ):  # the logest subarray is when the zero and the one is equal so we return the small count times two
        return zeros_count * 2
    else:
        return ones_count * 2


print(longest_subarray([1, 0, 1, 0, 0, 0, 1, 0, 0]))
