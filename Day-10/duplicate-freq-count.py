'''
duplicate elements :
    Duplicate elements are the values that appears more than once in the list/array
       ex : [1,2,2,3,4,4,5]
       o/p: [1,3,5](these elements do not repeat)
            [2,4] -> repeated elements

steps: 1. create an empty dictionary
2. count frequency of each number
3. if frequency==1 -> distinct
4. if frequency > 1-> duplicate
'''


arr=[1,2,2,3,4,4,5]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)



