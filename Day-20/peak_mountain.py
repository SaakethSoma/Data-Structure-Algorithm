def peak_mountain(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid] < arr[mid+1]:
            low=mid+1
        else:
            high=mid
    return arr[low]
arr=[1,3,5,7,6,4,2]
print(peak_mountain(arr))