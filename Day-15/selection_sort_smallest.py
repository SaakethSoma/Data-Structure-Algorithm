def selection_sort(arr,k):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k-1]
arr=[64, 34, 25, 12, 22, 11, 90]
k=int(input("Enter the value of k: "))
print("The", k, "smallest element is:", selection_sort(arr, k))