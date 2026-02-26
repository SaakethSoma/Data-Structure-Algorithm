'''
n=int(input("enter the size:"))
for row in range(1,n+1):
    for col in range(row):
        print("*",end=' ')
    print()
'''

def star_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end= ' ' )
        print()
def main():
    n=int(input("enter the size:"))
    star_pattern(n)
main()
