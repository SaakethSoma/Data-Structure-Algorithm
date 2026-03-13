def find_max(arr):
    maximum=arr[0]
    for num in arr:
        if num > maximum:
            maximum=num
    return maximum
def main():
    arr=[15,22,98,99,1]
    print("max:",find_max(arr))
main()
