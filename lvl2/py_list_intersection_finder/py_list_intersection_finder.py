"""
Write a function that finds the intersection of multiple sorted lists.
Return a new list containing elements that appear in ALL input lists, in sorted order.

The function should:
- Return elements that appear in ALL lists
- Result should be sorted in ascending order
- Remove duplicates from the result
- Handle empty input or empty lists gracefully
- If any list is empty, the intersection is empty
"""


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    return list(set(lists[0]).intersection(*lists[1:]))


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
    # [2, 3]

    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
    # [4]

    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
    # [1, 2, 3]

    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
    # []

    print(list_intersection_finder([]))
    # []

    print(list_intersection_finder([[1, 2, 3], []]))
    # []

    print(list_intersection_finder([[5]]))
    # [5]