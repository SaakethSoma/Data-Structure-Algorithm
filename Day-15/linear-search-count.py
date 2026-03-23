# arr=[50,30,20,30,10,30] target=30 output: 3 count of target element in the array
def linear_Search(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count

arr = [50, 30, 20, 30, 10, 30]
target = 30
result = linear_Search(arr, target)
print("Count of target element in the array:", result)