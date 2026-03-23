def two_sum(arr, target):
    left=0
    right=len(arr)-1
    while left<right:
        curr_sum=arr[left]+arr[right]
        if curr_sum==target:
            return arr[left], arr[right]
        elif curr_sum<target:
            left+=1 #increase sum
        else:
            right-=1 #decrease sum
    return None
arr=[1,2,3,4,6]
target=6
print("sum:", two_sum(arr, target))