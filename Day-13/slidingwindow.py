''' 
sliding winow: is a technique we used when we need to work with subarrays or substring of fixed /variable size effeciently.
instead of recalculating values for every subarray,we slide a window over an array.

approach:
1.start with the window(subset of array)
2.expand the window -> move to the right pointer
3.shrink the window -> move to the left pointer
4.maintain the required condition(sum,count, etc) 

'''
#counting subarrays of size k problem
#ex : [1,2,3,4,5] k=3 output : 3 (1,2,3) (2,3,4) (3,4,5)
def count_subarrays(arr,k):
    count=0
    for i in range(len(arr)):
        if i >= k-1:
            count+=1
    return count
def main():
    arr=[1,2,3,4,5]
    k=3
    print("subarrays count:", count_subarrays(arr,k))
main()
 