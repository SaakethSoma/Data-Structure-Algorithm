def find_sum(arr):
    total=0
    for num in arr:
        total+=num
    return total
def main():
    arr=[1,2,3,4,5]
    print("sum:",find_sum(arr))
main()
