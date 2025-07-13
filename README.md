# CS50P-Project : Student Budget Handler
My final project for the CS50P Python course.   
Video Demo:  <URL HERE>

## Description
**Student Budget Handler** is a Python-based application designed to help students effectively manage their monthly allowance. Whether it's tracking lunch expenses or budgeting for gifts, this tool provides a simple way to stay financially organized.

This program was developed as the final project for the **CS50P Python Programming course**, demonstrating how Python can be applied to real-life budgeting problems using file handling, data visualization, and formatted outputs.

## Key Features
- **Add Expenses by Category**  
    - The user can record their expenses under predefined categories: `Food`, `Stationery`, `Travel`, `Entertainment`, and `Gifts`. The program prompts for the category and amount spent, then saves the data to a CSV file that stores all previous entries. It continues to accept new entries until the user presses `Ctrl + D` to stop.

- **View Expense Summary**  
    - Users can view their expense history in a neat `tabular format`. Additionally, the program generates a `bar graph` that compares actual spending in each category with the user's monthly budget — giving a clear visual of where they might be overspending or saving.

- **Clear Expense History**  
    - In case a new user wants to start using the planner, or when a new month begins, the program allows clearing all past records so a fresh log can be maintained.

## Libraries Used

- `csv` – for handling expense data files  
- `matplotlib` – for plotting bar graphs  
- `tabulate` – for displaying tables in the terminal  
- `pyfiglet` – for stylized welcome text  
- `numpy` – used for numerical support in graph plotting


## How to Run the Program

1. **Install the required dependencies**  
   Open terminal and run: `pip install -r requirements.txt`

2. **Run the program**  
    Run: `python project.py`


## Usage Example

1. **Launch the program**  
- A stylized welcome message appears using `pyfiglet`.

2. **Select an option by number**  
- `1` – Add Expense  
- `2` – View Summary  
- `3` – Clear History  
- If invalid input is entered (like the option name or an incorrect number), the user is prompted again.

3. **Add Expense**  
- A list of categories is shown: `Food`, `Stationery`, `Travel`, `Entertainment`, `Gifts`.
- The user enters:
  - A valid category from the list
  - The amount spent (e.g., `150`)
- If **either** input is invalid (e.g., unlisted category, non-numeric or negative amount), the user is prompted to re-enter both.
- The user can continue entering multiple expenses. Pressing `Ctrl + D` stops the entry process.
4. **View Summary**  
- The user sees a full table of past expenses.
- A bar graph is generated and saved in a file 'expense_chart.png' comparing actual spending vs. the budget.

5. **Clear History**  
- Deletes all existing data from the CSV file for a fresh start.

---

