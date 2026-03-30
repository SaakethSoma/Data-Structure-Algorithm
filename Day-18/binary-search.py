'''
Binary Search : It is an efficient sorting algorithm used to find elements in a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the search interval is empty.
or list instead of checking each element one by one (like linear search)
Binary Search divides the search space into halves , making it much faster

It is divide and conquer algorithm that repeatedly divides the search interval in half &
comparing middle element with target value.

array must be in ascending or descending order

'''

def binary_search(arr, target):
    low=0 
    high=len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]: 
            high = mid - 1
        else:
            low = mid + 1
    return -1
arr=[10,20,30,40,50]
target=40
print("element found at index:",binary_search(arr,target))