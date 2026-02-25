'''
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if num1>num2:
    print("num1 is bigger")
else:
    print("num2 is bigger")
'''

def max_num(a,b):
    if a>b:
        print(f'{a} is bigger')
    else:
        print(f'{b} is bigger')
def main():
    a=int(input("emter the num:"))
    b=int(input("enter the num:"))
    max_num(a,b)
main()
