'''
rows = int(input("enter the rows:"))

for i in range(rows, 0, -1):
    spaces = rows - i
    print("  " * spaces, end="")   # left spaces (2 spaces for alignment)
    
    for j in range(i):
        print("*", end=" ")
    print()
'''

def star_pattern(n):
    for i in range(n):
        for j in range(n):
            if j<i:
                print(" ",end=' ')
            else:
                print("*",end=' ')
        print()
def main():
    n=int(input("enter the rows:"))
    star_pattern(n)
main()
            
