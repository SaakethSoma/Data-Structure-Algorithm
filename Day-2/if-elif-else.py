def check_grade(n):
    if n>91:
        print("O GRADE")
    elif n>80:
        print("A+ grade")
    elif n>70:
        print("A grade")
    elif n>60:
        print("B+ grade")
    elif n>50:
        print("B grade")
    elif n>40:
        print("C+ grade")
    else:
        print("fail")
def main():
    n=int(input("enter the marks:"))
    check_grade(n)
main()
