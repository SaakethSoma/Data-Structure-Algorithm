'''
bubble sort: one of the simplest sorting algorithms is bubble sort. 
It works by repeatedly swapping the adjacent elements if they are in the wrong order. 
large elements will "bubble" to the end of the list in each iteration.

how it works:
1)compare first and second element, swap if needed
2) move to the next pair
3) after one full pass -> largest element reaches to the end of the list
4) repeat for remaining elements until the list is sorted
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr  
arr=[8,4,7,3,1,5]
print(bubble_sort(arr))
