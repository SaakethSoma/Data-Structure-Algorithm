'''
a peak element is an element in an array that is greater than or equal to its neighbors.

formally : arr[i] >= arr[i-1] and arr[i] >= arr[i+1]

Edge cases:
1) first element -> compare only with right
2) last element -> compare only with left

optimal approach(binary search):
key insights : 1) if arr[mid] < arr[mid+1] -> peak is an right side
else -> peak is on left side(including mid)
'''

def find_peak(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid] < arr[mid+1]:
            low=mid+1
        else:
            high=mid
    return arr[low]
arr=[1,2,4,5,9,10]
print(find_peak(arr))