def find_second_max(arr):
    first=arr[0]
    second=arr[0]
    for num in arr:
        if num > first:
            second=first
            first=num
        elif num>second and num != first:
            second=num
    return second
def main():
    arr=[8,10,5,99,80]
    print("second largest number:",find_second_max(arr))
main()
