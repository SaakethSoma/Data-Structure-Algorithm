#subarray sum equals to k
arr=[1,2,3,4,5]
k=9
prefix=0
seen=set()
for num in arr:
    prefix+=num
    if prefix == k or (prefix-k) in seen:
        print("subarray exists")
        break
    seen.add(prefix)

#dry run
#prefix = 0, seen = {}
#num = 1, prefix = 1, 1==9 false, 1-9=-8 not in seen = {1}
#num = 2, prefix = 3, 3==9 false, 3-9=-6 not in seen = {1, 3}
#num = 3, prefix = 6, 6==9 false, 6-9=-3 not in seen = {1, 3, 6}
#num = 4, prefix = 10 , 10==9 false , 10-9=1 in seen true => subarray exists
