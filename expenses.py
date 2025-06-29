import csv

class Expenses:
    @classmethod
    def get_my_expense(cls):
        my_expense = []
        with open("my_expense.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                my_expense.append(row)
        return my_expense 

    @classmethod
    def write_my_expense(cls, my_expense):
        with open("my_expense.csv", 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Category','Your Expense'])
            for row in my_expense:
                writer.writerow(row)

    @classmethod
    def clear_my_expense(cls):
        cleared_expenses = [['Category', 'Your Expense'], ['Food', '0'], ['Stationary', '0'], ['Travel', '0'], ['Entertainment', '0', ], ['Gifts', '0']]
        with open("my_expense.csv", 'w') as file:
            writer = csv.writer(file)
            for row in cleared_expenses:
                writer.writerow(row)