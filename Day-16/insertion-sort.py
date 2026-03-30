'''
insertion sort: insertion sort is a simple sorting algorithm 
It works like sorting playing cards in your hands.
working: 1) assume the first element is sorted
2)pick the next element
3)comapre it with previous elements
4)shift large elements to the right
5)insert the picked element at the correct position
Time complexity: O(n^2) in worst case, O(n) in best case (when the array is already sorted)
Space complexity: O(1) (in-place sorting) 
'''
def insertion_sort(arr):
    count=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            count+=1
        arr[j + 1] = key
        countofi+=1
    return arr,count,countofi
arr=[8,3,2,4]
print(insertion_sort(arr))