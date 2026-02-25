'''
n=int(input("enter a number:"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")
'''

def check_num(n):
    if n %2==0:
        print("number is even")
    else:
        print("number is odd")
def main():
    n=int(input("enter the number:"))
    check_num(n)
main()
