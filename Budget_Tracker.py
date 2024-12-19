# Import all required Python modules
import sys
import matplotlib.pyplot as plt
from PIL import Image
import requests

# API Key for the currency conversion (source: FreeCurrencyAPI, https://freecurrencyapi.com/)
# For the API part we used resources from HSG course Computer Science as well as ChatGPT
API_KEY = "fca_live_mUgr0iesdfU3EbKI0GF8T4tnfARgaqJuPTVYlrk5"

# This function serves as the entry point to the program and displays the landing page.
# The user is prompted to input their budget and can then choose from five options.
def main():
    print("Welcome to your Expense Tracker!")
    budget = set_budget()
    expenses = {}
    # Main program loop for the user to interact with different functionalities.
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
            convert_currency(budget, expenses)
        elif choice == 5:
            print("Exiting Expense Tracker. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

# This function validates the user's budget input to ensure it is a positive number
# and handles invalid inputs (e.g., non-numeric or negative values).
def set_budget():
    while True:
        try:
            budget = float(input("Enter your monthly budget in CHF: "))
            if budget <= 0:
                raise ValueError("Budget must be greater than zero.")
            return budget
        except ValueError as e:
            print(f"Error: {e}")

# Prints the menu with five options for user interaction.
def print_menu():
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Visualize Expenses")
    print("4. Convert Remaining Budget to EUR")
    print("5. Exit")

# Retrieves and validates the user's menu choice, returning it as an integer.
# If the input is invalid, it defaults to returning 0.
def get_user_choice():
    try:
        return int(input("Enter your choice (1-5): "))
    except ValueError:
        return 0

# Option 1: Adds a new expense to the user's tracker.
# Prompts the user for a category and an amount, ensures the amount is positive and updates the expenses dictionary.
def add_expense(expenses):
    try:
        category = input("Enter expense category (e.g., Food, Rent): ").strip()
        amount = float(input(f"Enter amount for {category} in CHF: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        print(f"Added {amount:.2f} CHF to {category}.")
    except ValueError as e:
        print(f"Error: {e}")

# Option 2: Displays a summary of expenses and calculates the remaining budget.
# Alerts the user if the budget is exceeded or if spending is close to the limit.
def view_summary(expenses, budget):
    total_spent = sum(expenses.values())
    print("\nExpense Summary:")
    for category, amount in expenses.items():
        print(f"  {category}: {amount:.2f} CHF")
    print(f"Total Spent: {total_spent:.2f} CHF")
    print(f"Remaining Budget: {budget - total_spent:.2f} CHF")
    # Alert the user if they exceed their budget and display an image as a warning.
    if total_spent > budget:
        print("Alert: You have exceeded your budget!")
        show_image("download.jpg")
    elif total_spent > 0.9 * budget:
        # Warning for nearing the budget limit.
        print("Warning: You are about to exceed your budget!")

# Displays an image as a warning if the budget is exceeded.
# For this part we used ChatGPT
def show_image(image_path):
    """Display an image if the budget is exceeded."""
    from PIL import Image
    import os
    try:
        # Attempt to open and display the specified image file.
        print(f"Trying to open image at: {os.path.abspath(image_path)}")
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        # Handle errors if the image cannot be opened or displayed.
        print(f"Could not display image: {e}")

# Option 3: Visualizes the user's expenses using pie and bar charts.
# Shows spending by category and compares total spending to the remaining budget.
def visualize_expenses(expenses, budget):
    total_spent = sum(expenses.values())
    remaining_budget = max(budget - total_spent, 0)
    
    # Generate a pie chart for spending breakdown by category if expenses exist.
    if expenses:
        plt.figure(figsize=(8, 6))
        labels = list(expenses.keys())
        values = list(expenses.values())
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Spending Breakdown by Category")
        plt.show()
    else:
        print("No expenses to visualize yet.")

    # Generate a bar chart to show the remaining budget vs. total spending.
    plt.figure(figsize=(8, 6))
    labels = ['Spent', 'Remaining']
    values = [total_spent, remaining_budget]
    colors = ['#ff9999', '#66b3ff']
    plt.bar(labels, values, color=colors)
    plt.title("Budget Utilization")
    plt.ylabel("Amount (CHF)")
    plt.show()

# Option 4: Converts the remaining budget from CHF to EUR using an online currency API.
# If there is no remaining budget, informs the user.
def convert_currency(budget, expenses):
    total_spent = sum(expenses.values())
    remaining_budget = budget - total_spent
    if remaining_budget <= 0:
        # Notify the user if there is no remaining budget to convert.
        print("No remaining budget to convert. You have already exceeded your budget.")
        return
    try:
        # Fetch the current exchange rate from the API.
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
        # This part was added by ChatGPT to handle request errors.
        else:
            # Handle errors if the API request fails.
            print(f"Error: Failed to connect to the API (status code: {response.status_code}).")
    except Exception as e:
        # Handle unexpected errors during the API call.
        print(f"An error occurred: {e}")

# The main function is executed when the script is run directly.
if __name__ == "__main__":
    main()
# Used help from ChatGPT to structure the code, debugging as well as code comments.
# Additional information and detailed description is in the ReadMe file on GitHub.
