def two_sum_optimized(arr,target):
    target=9
    seen = set()
    
    for num in arr:
        diff = target - num

        if diff in seen:
            return True

        seen.add(num)

    return False
def main():
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))
    
    result = two_sum_optimized(arr, target)
    print("Pair:", result)

main()
