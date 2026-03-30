'''
inserting an element into a sorted array
arr=[1,3,5,7]
x=4
output=[1,3,4,5,7]

approach:
1.start from end of array
2.shift elements greater than x to the right
3.insert x at the correct position
'''


#inserting an element into a sorted array
def insert_into_sorted_array(arr, x):
    arr.append(0)
    i = len(arr) - 2
    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = x
    return arr
arr=[1,3,5,7]
x=4
print(insert_into_sorted_array(arr, x))