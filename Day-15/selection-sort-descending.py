def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
arr=[64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", selection_sort(arr))