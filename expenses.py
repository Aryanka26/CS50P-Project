import csv


class Expenses:
    @classmethod
    def get_my_expenses(cls):
        my_expenses = []
        with open("my_expenses.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                my_expenses.append(row)
        return my_expenses

    @classmethod
    def write_my_expenses(cls, my_expenses):
        with open("my_expenses.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Your Expense"])
            for row in my_expenses:
                writer.writerow(row)

    @classmethod
    def clear_my_expenses(cls):
        cleared_expenses = [
            ["Category", "Your Expense"],
            ["Food", "0"],
            ["Stationary", "0"],
            ["Travel", "0"],
            ["Entertainment", "0"],
            ["Gifts", "0"]
        ]
        with open("my_expenses.csv", "w") as file:
            writer = csv.writer(file)
            for row in cleared_expenses:
                writer.writerow(row)
