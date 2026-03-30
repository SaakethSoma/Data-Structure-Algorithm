def first_occurrence(arr, target):

    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid        # store answer
            right = mid - 1     # move left

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result


arr = [1,2,2,3,3,4,4]
target = 3

print(first_occurrence(arr, target))