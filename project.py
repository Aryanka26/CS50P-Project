def main():
    option = int(input("1.Add your expenses\n2.See the expense chart\n(Enter the option no. you wish to choose)\n"))
    if option == 1:
        add_expense()
    else:
        expense_chart()


def add_expense():
    print("Successfully in add_expense")


def expense_chart():
    print("Successfully in expense_chart")
    

if __name__ == "__main__":
    main()