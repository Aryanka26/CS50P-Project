from expenses import Expenses
import matplotlib.pyplot as plt
from pyfiglet import Figlet
import numpy as np
import csv


def main():
    figlet = Figlet(font="weird")
    print(figlet.renderText("|welcome|"))
    print(
        "1.Add your expenses\n2.See the expense chart\n3.Clear your expense history\n(Enter the option you wish to choose)"
    )
    while True:
        try:
            option = int(input())
            if option == 1:
                add_expenses()
                print(f"\nAll expenses added :)")
                break
            elif option == 2:
                expense_chart()
                print(
                    "Chart Updated Successfully!!!\nOpen 'expense_chart.png' to see the results :)"
                )
                break
            elif option == 3:
                Expenses.clear_my_expense()
                print("Your expenses history is cleared!!!")
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
            while True:
                try:
                    your_category = input("Enter Category: ")
                    your_expense = int(input("Expense: Rs."))
                    your_category, your_expense = validate_input(
                        your_category, your_expense
                    )
                    break
                except ValueError:
                    pass
            my_expense = Expenses.get_my_expense()
            my_expense.remove(my_expense[0])
            new_expense = append_expense(my_expense, your_category, your_expense)
            Expenses.write_my_expense(my_expense)
            print("Expense Added!! (Press Ctrl+D if you wish to exit)")
        except EOFError:
            break


def expense_chart(barwidth=0.25):
    fig = plt.subplots(figsize=(12, 8))

    your_expense, max_budget, categories = get_graph_input(
        Expenses.get_my_expense(), get_budget("max_budget.csv")
    )

    br1 = np.arange(len(your_expense))
    br2 = np.array(br1, dtype=float) + barwidth

    plt.bar(br1, your_expense, width=barwidth, edgecolor="black", label="Expense")
    plt.bar(br2, max_budget, color="r", width=barwidth, edgecolor="black", label="Budget")

    plt.title("Expenses Chart", fontsize=20, fontweight="bold")
    plt.xlabel("Category", fontweight="bold", fontsize=15)
    plt.ylabel("Expenses", fontweight="bold", fontsize=15)
    plt.xticks([r + (barwidth / 2) for r in range(len(your_expense))], categories)

    plt.legend()
    plt.savefig("expense_chart.png")
    plt.show()


def get_budget(filename):
    budget = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            budget.append(row)
    return budget


def append_expense(my_list, your_category, your_expense):
    for row in my_list:
        category = row[0]
        expense = int(row[1])
        if your_category == category:
            expense = expense + your_expense
            row[1] = expense
    return my_list


def get_graph_input(list1, list2):
    list1.remove(list1[0])
    your_expense = [int(row[1]) for row in list1]

    list2.remove(list2[0])
    max_budget = [int(row[1]) for row in list2]
    categories = [row[0] for row in list2]

    return your_expense, max_budget, categories


def validate_input(category, expense):
    category = category.strip().capitalize()
    categories = ["Food", "Stationary", "Travel", "Entertainment", "Gifts"]
    if not category in categories or not category:
        print("Invalid Category, did not add expense")
        raise ValueError()
    if expense < 0:
        print("Invalid Expense, did not add expense")
        raise ValueError()
    return category, expense


if __name__ == "__main__":
    main()
