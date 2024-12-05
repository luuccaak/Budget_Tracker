import sys
import matplotlib.pyplot as plt
from PIL import Image
import requests

# Your API Key for the FreeCurrencyAPI
API_KEY = "fca_live_mUgr0iesdfU3EbKI0GF8T4tnfARgaqJuPTVYlrk5"

def main():
    print("Welcome to the Expense Tracker!")
    budget = set_budget()
    expenses = {}
    while True:
        print_menu()
        choice = get_user_choice()
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_summary(expenses, budget)
        elif choice == 3:
            visualize_expenses(expenses, budget)
        elif choice == 4:
            convert_currency_with_api_key(budget, expenses)
        elif choice == 5:
            print("Exiting the Expense Tracker. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def set_budget():
    while True:
        try:
            budget = float(input("Enter your monthly budget in CHF: "))
            if budget <= 0:
                raise ValueError("Budget must be greater than zero.")
            return budget
        except ValueError as e:
            print(f"Error: {e}")

def print_menu():
    print("\nMenu:")
    print("1. Add an Expense")
    print("2. View Summary")
    print("3. Visualize Expenses")
    print("4. Convert Remaining Budget to EUR")
    print("5. Exit")

def get_user_choice():
    try:
        return int(input("Enter your choice (1-5): "))
    except ValueError:
        return 0  # Return invalid choice

def add_expense(expenses):
    try:
        category = input("Enter the expense category (e.g., Food, Rent): ").strip()
        amount = float(input(f"Enter the amount for {category} in CHF: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        print(f"Added {amount:.2f} CHF to {category}.")
    except ValueError as e:
        print(f"Error: {e}")

def view_summary(expenses, budget):
    total_spent = sum(expenses.values())
    print("\nExpense Summary:")
    for category, amount in expenses.items():
        print(f"  {category}: {amount:.2f} CHF")
    print(f"Total Spent: {total_spent:.2f} CHF")
    print(f"Remaining Budget: {budget - total_spent:.2f} CHF")
    if total_spent > budget:
        print("Alert: You have exceeded your budget!")
        show_image_on_budget_exceeded("download.jpg")
    elif total_spent > 0.9 * budget:
        print("Warning: You are about to exceed your budget!")

def show_image_on_budget_exceeded(image_path):
    """Display an image if the budget is exceeded."""
    from PIL import Image
    import os
    try:
        print(f"Trying to open image at: {os.path.abspath(image_path)}")
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Could not display image: {e}")

def visualize_expenses(expenses, budget):
    total_spent = sum(expenses.values())
    remaining_budget = max(budget - total_spent, 0)
    
    # Pie Chart for Expense Categories
    if expenses:
        plt.figure(figsize=(8, 6))
        labels = list(expenses.keys())
        values = list(expenses.values())
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Spending Breakdown by Category")
        plt.show()
    else:
        print("No expenses to visualize yet.")

    # Bar Chart for Budget vs Spent
    plt.figure(figsize=(8, 6))
    labels = ['Spent', 'Remaining']
    values = [total_spent, remaining_budget]
    colors = ['#ff9999', '#66b3ff']
    plt.bar(labels, values, color=colors)
    plt.title("Budget Utilization")
    plt.ylabel("Amount (CHF)")
    plt.show()

def convert_currency_with_api_key(budget, expenses):
    total_spent = sum(expenses.values())
    remaining_budget = budget - total_spent
    if remaining_budget <= 0:
        print("No remaining budget to convert.")
        return
    try:
        # Use FreeCurrencyAPI with API key
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency=CHF"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "EUR" in data["data"]:
                eur_rate = data["data"]["EUR"]
                remaining_eur = remaining_budget * eur_rate
                print(f"Remaining Budget: {remaining_budget:.2f} CHF")
                print(f"Equivalent in EUR: {remaining_eur:.2f} EUR")
            else:
                print("Error: Unable to fetch conversion rate.")
        else:
            print(f"Error: Failed to connect to the API (status code: {response.status_code}).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
