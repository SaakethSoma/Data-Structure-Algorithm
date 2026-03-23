#find the minimum sum of any subarray of size k
#input:arr=[2,1,5,1,3,2]  k=3
#output: 6
def min_sum_subarray(arr,k):
    window_Sum=0
    min_Sum=float('inf')
    for i in range(len(arr)):
        window_Sum+=arr[i]
        if i >= k-1:
            min_Sum=min(min_Sum,window_Sum)
            window_Sum-=arr[i-k+1]
    return min_Sum
def main():
    arr=[2,1,5,1,3,2]
    k=3
    print("min sum of subarray of size k:", min_sum_subarray(arr,k))
main()