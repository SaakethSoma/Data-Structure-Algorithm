def find_min(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid-1
    return arr[low]

arr=[4,5,6,7,0,1,2]
print(find_min(arr))