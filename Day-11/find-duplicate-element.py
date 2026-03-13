'''
arr=[1,1,2,2,3,4,5]
result=[]              #o/p: 1,2
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in freq:
    if freq[key]>1:
        result.append(key)
print(result)
'''

'''
arr=[1,1,2,2,3,4,5]   #o/p : 3 4 5

freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in freq:
    if freq[key]==1:
        print(key,end=" ")
'''


arr=[1,1,2,2,3,4,5]    #o/p:1,2

freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in freq:
    if freq[key]>1:
        print(key,end=" ")



