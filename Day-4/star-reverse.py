'''
n = int(input("Enter number of rows: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
'''
def star_pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=' ')
        print()

def main():
    n=int(input("enter the size:"))
    star_pattern(n)
main()
