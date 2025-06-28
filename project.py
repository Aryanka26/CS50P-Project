import csv


def main():
    option = int(input("1.Add your expenses\n2.See the expense chart\n3.Clear your expense history\n(Enter the option no. you wish to choose)\n"))
    if option == 1:
        add_expenses()
        print(f"Expense added!!!")
    elif option == 2:
        expense_chart()
    else:
        clear_my_expense()
        print("History cleared!!!")


def add_expenses():
    print("Successfully in add_expense")
    your_category = input("Enter Category: ").strip().capitalize()
    your_expense = int(input("Expense: "))

    my_expense = get_my_expense()
    my_expense.remove(my_expense[0])
    print(my_expense)

    for row in my_expense:
        category = row[0]
        expense = int(row[1])
        if your_category == category:
            expense = expense + your_expense
            row[1] = expense

    print(my_expense)
    write_my_expense(my_expense)   
    

def expense_chart():
    print("Successfully in expense_chart")



def get_budget():
    budget = []
    with open("max_budget.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            budget.append(row)
    return budget


def get_my_expense():
    my_expense = []
    with open("my_expense.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            my_expense.append(row)
    return my_expense 


def write_my_expense(my_expense):
    with open("my_expense.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Category','Your Expense'])
        for row in my_expense:
            writer.writerow(row)


def clear_my_expense():
    cleared_expenses = [['Category', 'Your Expense'], ['Food', '0'], ['Stationary', '0'], ['Travel', '0'], ['Entertainment', '0', ], ['Gifts', '0']]
    with open("my_expense.csv", 'w') as file:
        writer = csv.writer(file)
        for row in cleared_expenses:
            writer.writerow(row)


if __name__ == "__main__":
    main()