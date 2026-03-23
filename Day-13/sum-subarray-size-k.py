#sum of subarray of size k
#input: arr=[1,2,3,4,5], k=3
#output: [6,9,12]
def sum_subarray(arr,k):
    window_Sum=0
    result=[]
    for i in range(len(arr)):
        window_Sum+=arr[i]
        if i >= k-1:
            result.append(window_Sum)
            window_Sum-=arr[i-k+1]
    return result 
def main():
    arr=[1,2,3,4,5]
    k=3
    print("sum of subarray of size k:", sum_subarray(arr,k))
main()