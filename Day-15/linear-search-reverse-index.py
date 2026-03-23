def linear_Search(arr):
    for i in range(len(arr)):
        if arr[i] <0:
            return arr[i]
    return None
arr=[0,30,-2,-4,-7]
print("element found at index:", linear_Search(arr))