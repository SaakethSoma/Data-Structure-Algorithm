#find the maximum sum of any subarray of size k
def max_sum_subarray(arr,k):
    window_Sum=0
    max_Sum=0
    for i in range(len(arr)):
        window_Sum+=arr[i]
        if i >= k-1:
            max_Sum=max(max_Sum,window_Sum)
            window_Sum-=arr[i-k+1]
    return max_Sum
def main():
    arr=[2,1,5,1,3,2]
    k=3
    result = max_sum_subarray(arr,k)
    print("max sum of subarray of size k:", result)
main()