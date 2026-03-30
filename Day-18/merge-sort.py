'''
merge sort: 
IDEA : 1) divide the array into two halves
        2) recursively sort each half
        3) merge the sorted halves

key concepts: 1) always splits then merges with sorted arrays 

time complexity: O(n log n) in all cases [best,average,worst]

proof :whenever we chekc every element in the array, we have O(n) time complexity , 
dividing time complexity is O(log n) = O(n) + O(log n) = O(n log n)

'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr=[5,2,4,1]
sorted_arr=merge_sort(arr)
print("original array:",arr)
print("sorted array:",sorted_arr)
