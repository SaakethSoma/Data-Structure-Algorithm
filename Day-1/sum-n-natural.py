def calculate_sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
def main():
    n=int(input("enter no:"))
    print("Sum:",calculate_sum(n))
if __name__=="__main__":
    main()

        
    
