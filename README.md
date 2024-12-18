# Budget Tracker

A simple and interactive expense tracker tool to manage your monthly budget, visualize expenses, and convert remaining budgets into different currencies.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [How to Use](#how-to-use)
6. [Credits](#credits)
7. [License](#license)

---

## Project Description
This **Budget Tracker** project is a Python-based tool designed to help users:
- Set and manage their monthly budget.
- Add and track expenses.
- Visualize expenses using charts.
- Convert the remaining budget into a different currency (EUR) using a live API.

### Motivation
Managing a personal budget efficiently can be challenging. This project provides a user-friendly, interactive tool to keep track of expenses, analyze where money is going, and make better financial decisions.

---

## Features
- **Set Monthly Budget:** Allows users to set a budget for a month.
- **Add Expenses:** Add and categorize expenses interactively.
- **View Summary:** Displays a summary of all expenses and remaining budget.
- **Expense Visualization:** Generates visual charts (using `matplotlib`) for better understanding.
- **Currency Conversion:** Converts remaining budget into EUR using the [FreeCurrencyAPI](https://freecurrencyapi.com/).
- **Error Handling:** Handles invalid inputs and ensures a smooth user experience.

---

## Technologies Used
- **Python 3**: Programming language
- **matplotlib**: For visualizing expenses
- **requests**: To fetch currency conversion data from the API
- **Pillow (PIL)**: Image handling (optional functionality)
- **FreeCurrencyAPI**: External API for live currency exchange rates

---

## Installation
Follow these steps to set up and run the Budget Tracker locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/budget-tracker.git
   cd budget-tracker
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```bash
   python Budget_Tracker.py
   ```

---

## How to Use
1. **Run the Script:** Start the program in your terminal or command prompt.
2. **Set Budget:** Enter your monthly budget in CHF (Swiss Franc).
3. **Choose an Option from the Menu:**
   - **1:** Add an expense (Name and Amount).
   - **2:** View a summary of expenses and remaining budget.
   - **3:** Visualize expenses with a chart.
   - **4:** Convert remaining budget into EUR.
   - **5:** Exit the program.

### Example
```
Welcome to your Expense Tracker!
Enter your monthly budget in CHF: 1000

Menu:
1. Add Expense
2. View Summary
3. Visualize Expenses
4. Convert Remaining Budget to EUR
5. Exit

Your choice: 1
Enter expense name: Rent
Enter amount: 700
Expense added successfully!
```

---

## Credits
This project was developed as part of a learning exercise during the **HSG Introduction Into Programming Course**. This Project is based on the lessons-learned from the course. Additionally ChatGPT was used for debugging and code structure.

### Contributors
- **luuccaak** - [GitHub](https://github.com/luuccaak)
- **Ivcq** - [GitHub](https://github.com/Ivcq)

### API Provider
- [FreeCurrencyAPI](https://freecurrencyapi.com/)

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Future Improvements
- Add support for multiple currencies.
- Introduce expense categories for better organization.
- Add a graphical user interface (GUI) for an enhanced user experience.
