def count_even(arr):
    count=0
    for num in arr:
        if num %2==0:
            count+=1
    return count
def main():
    arr=[2,4,5,7,8,10]
    print("even count:",count_even(arr))
main()
