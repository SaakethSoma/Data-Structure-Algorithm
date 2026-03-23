#find the average of all the subarrays of sum k
#input:arr=[1,2,3,4,5], k=3
#output:[2.0,3.0,4.0]
def avg_subarray(arr,k):
    window_Sum=0
    result=[]
    for i in range(len(arr)):
        window_Sum+=arr[i]
        if i >= k-1:
            result.append(window_Sum/k)
            window_Sum-=arr[i-k+1]
    return result
def main():
    arr=[1,2,3,4,5]
    k=3
    print("average of subarray of size k:", avg_subarray(arr,k))
main()
