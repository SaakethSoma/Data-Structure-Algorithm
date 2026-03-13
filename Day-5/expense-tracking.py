expenses=[]
def show_menu():
    print("expenses tracker")
    print("1.add expense")
    print("2. view expenses")
    print("3.exit")
    
def add_expense():
    name=input("enter expense name:")
    try:
        amount=float(input("enter amount:"))
    except ValueError:
        print("Invalid amount. please enter a number:")
        return
    expense={
        "name": name,
        "amount": amount
    }
    expenses.append(expense)
    print("expenses added successfully.")

def view_expenses():
    if not expenses:
        print("no expenses found.")
        return
    print("-----expenses list-----")
    total=0
    for expense in expenses:
        print(f"{expense['name']} {expense['amount']}")
        total+=expense["amount"]
    print("total expense:{expense}",total)
def main():
    while True:
        show_menu()
        choice=input("enter the choice:")
        if choice== "1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            print("exiting....thank you")
        else:
            print("invalid choice.please try again")
if __name__=="__main__":
    main()
            
            
            
    
    
