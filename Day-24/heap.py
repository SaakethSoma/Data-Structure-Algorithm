'''
import heapq

heap = []

#Insert
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
print(heap)

#remove smallest
print(heapq.heappop(heap))
#peek
print(heap[0])

'''


'''
#Converting List to Heap
import heapq
arr = [10, 3, 7, 1]
heapq.heapify(arr)
print(arr)
'''

'''
import heapq
heap = []

heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -20)

print(-heapq.heappop(heap))
'''

'''
import heapq
def k_largest(arr, k):
    return heapq.nlargest(k, arr)
print(k_largest([10,4,3, 7, 20], 2))
''' 

'''
import heapq
def k_smallest(arr, k):
    return heapq.nsmallest(k, arr)
print(k_smallest([10,4,3, 7, 20], 2))
'''
