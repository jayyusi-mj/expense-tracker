expenses = []

def add_expense(amount, category):
    expenses.append([amount, category])
    print("Added:", amount, "-", category)

def show_expenses():
    for item in expenses:
        print(item[0], "-", item[1])

def total_expenses():
    total = 0
    for item in expenses:
        total = total + item[0]
    return total

while True:
    print("1: add expense, 2: show all, 3: total, 4: quit")
    choice = input("Choose: ")
    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        add_expense(amount, category)
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Total:", total_expenses())
    elif choice == "4":
        break