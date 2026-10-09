import json

expenses = []


def add_expense():
    name = input("Add an expense name: ")

    if not name:
        raise ValueError("Expense name cannot be empty.")

    try:
        amount = float(input("Enter an amount for your expense: "))

        if amount <= 0:
            raise ValueError("Expense amount must be greater than 0.")

        category = input("Enter the category for your expense: ")

        if not category:
            raise ValueError("Category cannot be empty.")

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added successfully.")

    except ValueError as error:
        print(f"Error: {error}")

    finally:
        print("Finished entering expense.")


def view_expenses():
    if not expenses:
        print("Please enter your expenses.")
        return

    print("Your Expenses")

    for expense in expenses:
        print(
            f"Name: {expense['name']} | "
            f"Category: {expense['category']} | "
            f"Amount: £{expense['amount']:.2f}"
        )


def calculate_total():
    total_expense = sum(
        expense["amount"] for expense in expenses
    )

    return f"The total amount for these expenses is: £{total_expense:.2f}"


def show_category():
    category = input("Enter the category: ")

    if not category.strip():
        print("Error: Category cannot be empty.")
        return

    total_category = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"] == category
    )

    print(f"Total: £{total_category:.2f}")


def delete_expense():
    if not expenses:
        print("There are no expenses to delete.")
        return

    name = input("Enter the name of the expense you want to delete: ")

    for expense in expenses:
        if expense["name"] == name:
            expenses.remove(expense)

            with open("expenses.json", "w") as file:
                json.dump(expenses, file, indent=4)

            print("Expense deleted successfully.")
            return

    print("Expense not found.")