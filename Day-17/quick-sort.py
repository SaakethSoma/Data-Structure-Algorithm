'''
quick sort: Quick Sort is a fast sorting algorithm that uses the idea of divide and conquer.

idea: 1)pick a pivot, 
2) place pivot in correct position,
3) element < pivot to left, 
4) element > pivot to right 

key concept : partitioning the array around the pivot

time complexity: O(n log n) on average, 
O(n^2) in worst case , 
o(n log n) in best case

space complexity: O(log n) on average
O(n) in worst case 
O(log n) in best case

'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left=[]
    right=[]
    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)
arr=[5,2,4,1]
print(quick_sort(arr))