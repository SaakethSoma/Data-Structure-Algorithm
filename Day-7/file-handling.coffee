expenses = []

def export_expenses(expenses):
    with open('expenses.txt','w') as file:
        for expense in expenses:
            line = expense["name"]+"-"+expense["amount"] + "\n"
            file.write(line)
    print("Export Completed")
    
def main():
    while True:
        print("-----Expense Tracker------")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Export to File")
        print("4. Exit")
        
        choise = input("Enter Your Choice:")
        
        if choise == "1":
            name = input("Enter Expense Name: ")
            amount = int(input("Enter Amount:"))
            expenses.append({
                "name" : name,
                "amount" :amount
            })
            print("Expense Added Successfully")
            
        elif choise == "2":
            if not expenses:
                print("No Expense")
            else:
                print("------Expense list-----")
                for expense in expenses:
                    print(expense["name"],"-", expense["amount"])
                    
        elif choise == '3':
            if not expenses:
                print("No Expenses to export")
            else:
                export_expenses(expenses)
        
        elif choise == "4":
            print("Exiting Program")
            break
        else:
            print("Invalid Choise")
main()