import csv
from datetime import datetime

categories = ['food', 'transport', 'utilities', 'entertainment', 'health', 'family/friends']
file_name = 'expenses.csv'
def add_expense():

    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter the description: ")
    category = input(f"Enter the category: ").lower()

    if category not in categories:
        print(f"Invalid category. Don't spend money on {category}!")
        return
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, description, category])
    print(f"Expense added: {date}, {amount}, {description}, {category}")

def view_expenses():
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            for row in reader:
                print(f"Date: {row[0]}, Amount: ₹{row[1]}, Description: {row[2]}, Category: {row[3]}")
    except FileNotFoundError:
        print("No expenses recorded.")

def total_spent():
    total = 0.0
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
            print(f"Total spent: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded.")


def main():
    print("Welcome to the Expenses Tracker!")
    print("Choose an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spent()
        elif choice == '4':
            print("Exiting the Expenses Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()