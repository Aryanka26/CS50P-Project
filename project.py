from expenses import Expenses
import matplotlib.pyplot as plt
from pyfiglet import Figlet
from tabulate import tabulate
import numpy as np
import csv

MENU = """1.Add expense
2.View Summary
3.Clear History

(Enter the option you wish to choose)
"""

CATEGORIES = """Categories :-
-Food
-Stationary
-Travel
-Entertainment
-Gifts
"""


# main function
def main():
    # prints a "welcome message"
    figlet = Figlet(font="weird")
    print(figlet.renderText("|welcome|"))

    # Asks user for an option
    print(MENU)
    while True:
        try:
            option = int(input())
            if option == 1:
                add_expenses()
                print(f"\nAll expenses added :)")
                break
            elif option == 2:
                expense_chart()
                print("Chart Updated!\nOpen 'expense_chart.png' to see the results :)")
                break
            elif option == 3:
                Expenses.clear_my_expenses()
                print("Your expenses history is cleared!!!")
                break
            else:
                print("Value not 1, 2 or 3")
                raise ValueError()
        except ValueError:
            print("Please enter an integer")
            pass


# option 1
def add_expenses():
    print("In add expenses...")
    print(CATEGORIES)

    # This loop is used to allow the user to add multiple expenses until they press 'Ctrl + D'
    while True:
        try:
            # asks user to enter category and amount spent.
            while True:
                try:
                    your_category = input("Enter Category: ")
                    your_expense = int(input("Enter Amount Spent: Rs."))
                    your_category, your_expense = validate_input(
                        your_category, your_expense
                    )
                    break
                except ValueError:
                    pass

            # adds the expenses according to the category to my_expenses csv file
            my_expenses = Expenses.get_my_expenses()
            my_expenses.remove(my_expenses[0])
            new_expenses = append_expense(my_expenses, your_category, your_expense)
            Expenses.write_my_expenses(new_expenses)

            print("Expense Added!! (Press Ctrl+D if you wish to exit)\n")
        except EOFError:
            break


# option 2
def expense_chart(barwidth=0.25):
    # shows user's expense history in a tabular format
    print("Your expenses so far..")
    print(table_format(Expenses.get_my_expenses()))

    # generates a graph comparing user's expenses to their budget

    # generates a figure of size 12 by 8
    fig = plt.subplots(figsize=(12, 8))

    # gets the necessary lists for generating graphs
    your_expenses, max_budget, categories = get_graph_input(
        Expenses.get_my_expenses(), get_budget("max_budget.csv")
    )

    # lists containing positions of each bar, br1 for user's expenses and br2 for the budget
    br1 = np.arange(len(your_expenses))
    br2 = np.array(br1, dtype=float) + barwidth

    # plots bar graphs
    plt.bar(br1, your_expenses, width=barwidth, edgecolor="black", label="Expense")
    plt.bar(
        br2, max_budget, color="r", width=barwidth, edgecolor="black", label="Budget"
    )

    # adds title and labels
    plt.title("Expenses Chart", fontsize=20, fontweight="bold")
    plt.xlabel("Category", fontweight="bold", fontsize=15)
    plt.ylabel("Expenses", fontweight="bold", fontsize=15)
    plt.xticks([r + (barwidth / 2) for r in range(len(your_expenses))], categories)

    # adds a legend
    plt.legend()
    # saves the graph in a file
    plt.savefig("expense_chart.png")
    plt.show()


# gets a list of budget from csv file
def get_budget(filename):
    budget = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            budget.append(row)
    return budget


# adds expense entered by user
def append_expense(my_list, your_category, your_expense):
    for row in my_list:
        category = row[0]
        expense = int(row[1])
        if your_category == category:
            expense = expense + your_expense
            row[1] = expense
    return my_list


# gets necessary graph inputs
def get_graph_input(list1, list2):
    list1.remove(list1[0])
    your_expense = [int(row[1]) for row in list1]

    list2.remove(list2[0])
    max_budget = [int(row[1]) for row in list2]
    categories = [row[0] for row in list2]

    return your_expense, max_budget, categories


# validates category and amount spent
def validate_input(category, expense):
    category = category.strip().capitalize()
    categories = ["Food", "Stationary", "Travel", "Entertainment", "Gifts"]
    if not category in categories or not category:
        print("Invalid Category, did not add expense\n")
        raise ValueError()
    if expense < 0:
        print("Invalid Expense, did not add expense\n")
        raise ValueError()
    return category, expense


# changes the list into a tabular format
def table_format(lst):
    header = lst.pop(0)
    return tabulate(lst, header, tablefmt="grid")


if __name__ == "__main__":
    main()
