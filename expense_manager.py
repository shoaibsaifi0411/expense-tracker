# GENerate_manager.py
file_name = "expenses.txt"

#function to add expense
def add_expense(date, category, amount, note):

    file = open(file_name, "a")

    record = date + "," + category + "," + str(amount) + "," + note + "\n"

    file.write(record)

    file.close()

# function to view/read expenses
def get_expenses():

    expenses = []

    try:
        file = open(file_name, "r")

        for line in file:
            data = line.strip().split(",")

            expense = {
                "date": data[0],
                "category": data[1],
                "amount": float(data[2]),
                "note": data[3]
            }

            expenses.append(expense)

        file.close()

    except:
        pass
    return expenses



#function to calculate total expenses
def total_expenses(expenses):
    expenses = get_expenses()
    total = 0
    for e in expenses:
        total += e["amount"]
    return total


#function for expenses wise category
def category_expenses(expenses):
    expenses = get_expenses()
    category_data = {}

    for e in expenses:
        category = e["category"]
        amount = e["amount"]

        if category in category_data:
            category_data[category] += amount
        else:
            category_data[category] = amount

    return category_data