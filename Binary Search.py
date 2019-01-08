def binary_search_i(in_list, target, key=None):

    # If a key is not given, construct the key to return its argument
    if key is None:
        key = lambda x: x

    # Initialise bounds
    lower_idx = 0
    upper_idx = len(in_list)

    # Check target is within the range in_list[lower_idx:upper_idx]
    if not key(in_list[lower_idx]) <= target <= key(in_list[upper_idx-1]):
        return -1

    # Repeat until range of values to search is empty.
    while upper_idx > lower_idx:
        # split at midpoint, get value at the midpoint.
        mid_idx = (lower_idx + upper_idx) // 2
        test_value = key(in_list[mid_idx])

        # Compare to target, return index if found
        if test_value == target:
            return mid_idx
        # Otherwise, narrow range to search.
        elif test_value > target:
            upper_idx = mid_idx
        else:
            lower_idx = mid_idx + 1
    return -1


def binary_search_r(in_list, target, lower_idx=0, upper_idx=None, key=None):

    # If an upper_idx is not given, take whole list
    if upper_idx is None:
        upper_idx = len(in_list)

    # If a key is not given, construct the key to return its argument
    if key is None:
        key = lambda x: x

    # Check target is within the range in_list[lower_idx:upper_idx]
    if not key(in_list[lower_idx]) <= target <= key(in_list[upper_idx-1]):
        return -1

    # split at midpoint, get value at the midpoint.
    mid_idx = (lower_idx + upper_idx) // 2
    test_value = key(in_list[mid_idx])

    # Compare to target, return index if found
    if test_value == target:
        return mid_idx

    # Otherwise, narrow range to search.
    elif test_value > target:
        return binary_search_r(in_list, target, lower_idx, mid_idx, key)
    else:
        return binary_search_r(in_list, target, mid_idx+1, upper_idx, key)
