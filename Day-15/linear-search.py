def linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

arr=[50,30,20,40,10]
target=20
print("element found at index:", linear_Search(arr, target))
