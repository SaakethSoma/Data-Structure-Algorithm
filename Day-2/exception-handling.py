try:
    num=int(input("enter the number:"))
    result= 10/num
    print("result",result)
except ZeroDivisionError:
    print("error: cannot divide by zero")
except ValueError:
    print("value is not defined")
finally:
    print("program ended")
