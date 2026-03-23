'''
prefix sum : it is a technique used to quickly calculate the sum of elements in a range of an array
ex: [2,4,6,8,10]
prefix = [2,6,12,20,30]
explanation :
prefix[0]=2
prefix[1]=2+4=6
prefix[2]=2+4+6=12
prefix[3]=2+4+6+8=20
prefix[4]=2+4+6+8+10=30

formula : prefix[i] = prefix[i-1] + arr[i]

to find the sum of elements from LEFT TO RIGHT : sum(left,right) = prefix[right] - prefix[Left-1]
prefix sum approach : pre-compute once -O(n) , Each query : O(1)

used in : 1. range sum queries 2.subarray problems 3. competitive programming 4.sliding window optimization
'''
