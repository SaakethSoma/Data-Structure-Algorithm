
##Brute Force Approach: solving a problem by using straight forward method.
##Trying every combination
##Making every possibility

##Solution for BFA is optimized approach and to reduce time complexity by
# a)using proper data structure
# b)sorting
# c)hashing
# d)mathematical methods

##DISADVANTAGES--using nested loop 0(n square)


def pair_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return True

    return False

def main():
    arr = [2,7,11,13]
    target = 9
    print("sol: ",pair_sum(arr,target))

main()
