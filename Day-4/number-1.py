'''
rows = int(input("Enter number of rows: "))

for i in range(1, rows +1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
'''

def star_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def main():
    n=int(input("Enter number of rows: "))
    star_pattern(n)
main()
