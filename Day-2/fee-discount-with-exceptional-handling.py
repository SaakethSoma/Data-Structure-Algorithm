def calculate_fee(course,marks):
    course=course.strip().lower()
    if course=="ai":
        fee=50000
    elif course=="web":
        fee=40000
    elif course=="data science":
        fee=45000
    else:
        return None

    if marks>90:
        print("discounted applied : 5000")
        fee-=5000
    return fee
def main():
    print("student fee calculator")
    course=input("enter the course(ai/web/data science):")
    try:
        marks=int(input("enter marks:"))
        if marks<0 or marks>100:
            print("invalid marks.please enter from 0-100.")
            return
    except ValueError:
        print("invalid input. marks must be a number")
        return
    fee=calculate_fee(course,marks)
    if fee is None:
        print("Invalid Course")
    else:
        print("final fee:",fee)
main()
        
