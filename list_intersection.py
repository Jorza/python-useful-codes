def intersection(list1, list2):
    """
    Return a sorted list that contains only the shared values of list1 and list2.

    Returned list has unique values, even if values are repeated in input lists.
    :param list1: input list 1
    :param list2: input list 2
    :return: sorted list of unique shared values in input lists.
    """

    list1.sort()
    list2.sort()
    idx1 = 0
    idx2 = 0
    out_list = []
    while idx1 < len(list1) and idx2 < len(list2):
        while idx1 < len(list1) and idx2 < len(list2) and list1[idx1] < list2[idx2]:
            idx1 += 1
        while idx1 < len(list1) and idx2 < len(list2) and list1[idx1] > list2[idx2]:
            idx2 += 1
        if idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1] == list2[idx2] and list1[idx1] not in out_list:
                out_list.append(list1[idx1])
                idx2 += 1
    return out_list


if __name__ == '__main__':
    # test cases
    list_pairs = [([], []),
                  ([], [2, 7, 3, 4, 6, 9]),
                  ([2, 6, 3, 4, 7, 5], [2, 7, 3, 4, 6, 9]),
                  ([0, 3, 4, 5, 8, 10], [1, 2, 3, 5, 6, 7, 9, 10, 11]),
                  ([0, 3, 5], [1, 5, 6])
                  ]
    expected_intersections = [
        [],
        [],
        [2, 3, 4, 6, 7],
        [3, 5, 10],
        [5]
    ]
    for index, list_pair in enumerate(list_pairs):
        assert intersection(list_pair[0], list_pair[1]) == expected_intersections[index]
