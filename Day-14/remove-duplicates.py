def remove_duplicates(arr):
    i=0
    for j in range(1, len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1
arr=[1,1,2,2,3]
k=remove_duplicates(arr)
print("new values:", k)
print("new array:", arr[:k])