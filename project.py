from expenses import Expenses
import csv


def main():
    print("1.Add your expenses\n2.See the expense chart\n3.Clear your expense history\n(Enter the option you wish to choose)")
    while True:
        try:
            option = int(input())
            if option == 1:
                add_expenses()
                print(f"Expense added!!!")
                break
            elif option == 2:
                expense_chart()
                break
            elif option == 3:
                Expenses.clear_my_expense()
                print("History cleared!!!")
                break
            else:
                print("Value not 1, 2 or 3")
                raise ValueError()
        except ValueError:
            print("Please enter an integer")
            pass


def add_expenses():
    print("In add expenses...")
    print("Categories :-\n-Food\n-Stationary\n-Travel\n-Entertainment\n-Gifts")
    while True:
        try:
            your_category = input("Enter Category: ").strip().capitalize()
            your_expense = int(input("Expense: Rs."))
            if not your_category:
                print("Please enter valid category")
                raise ValueError
            break
        except ValueError:
            pass
    my_expense = Expenses.get_my_expense()
    my_expense.remove(my_expense[0]) 
    for row in my_expense:
        category = row[0]
        expense = int(row[1])
        if your_category == category:
            expense = expense + your_expense
            row[1] = expense        
    Expenses.write_my_expense(my_expense)   
    

def expense_chart():
    print("Successfully in expense_chart")



def get_budget():
    budget = []
    with open("max_budget.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            budget.append(row)
    return budget





if __name__ == "__main__":
    main()