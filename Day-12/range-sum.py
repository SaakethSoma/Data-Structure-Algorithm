arr=[1, 2, 3, 4, 5]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
       

L=1
R=3
if L == 0:
    print(prefix[R])
else:
    print(prefix[R] - prefix[L-1])

#dry run
#prefix = [0,0,0,0,0]
#prefix[0] = arr[0] = 1
#prefix[1] = prefix[0] + arr[1] = 1 + 2 = 3
#prefix[2] = prefix[1] + arr[2] = 3 + 3 = 6
#prefix[3] = prefix[2] + arr[3] = 6 + 4 = 10
#prefix[4] = prefix[3] + arr[4] = 10 + 5 = 15 
#L=1, R=3

#sum(1,3) = prefix[3] - prefix[0] = 10 - 1 = 9
