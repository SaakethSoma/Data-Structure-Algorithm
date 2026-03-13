#returning indices of two strings

def two_sum_indices(arr,target):
    hashmap={}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashmap:
            return hashmap[diff],i
        hashmap[num] = i
    return None
def main():
    arr=[2,7,11,13]
    target = 9
    print("Indexes:",two_sum_indices(arr,target))
main()


'''
i=0
diff = 24-2 = 22
(2,0)
i=1
diff= 24-7=17
(7,1)
diff = 24-11=13
(11,2)
diff= 24-13=11
(2,3)
'''
