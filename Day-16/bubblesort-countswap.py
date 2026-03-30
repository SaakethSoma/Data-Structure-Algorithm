def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:     
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swap_count += 1
        if not swapped:
            break
    return arr, swap_count
arr = [9,3,5,1,6,]
sorted_arr, total_swaps = bubble_sort(arr)
print("Sorted array:", sorted_arr)
print("Total swaps:", total_swaps)