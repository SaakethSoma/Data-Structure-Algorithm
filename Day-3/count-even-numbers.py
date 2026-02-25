def count_even(n):
    count=0
    for i in range(1,n+1):
        if i %2==0:
            count+=1
    return count
def main():
    n=int(input("enter the number:"))
    print("even count:",count_even(n))
main()
