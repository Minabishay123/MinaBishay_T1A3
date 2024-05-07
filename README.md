# Personal Finance Tracker

## System Requirements

- **Operating System:** Any OS that can run Python (Windows, macOS, Linux, etc.)
- **Python version:** Python 3.10 or higher

## Installation

1. Download the source code from the repository or location it is hosted.
2. Navigate to the directory where the source code is located in your terminal or command prompt.

## Dependencies

Your application requires the following Python packages:

- `json`: This is a built-in Python package, so you don’t need to install it separately.
- `random`: This is a built-in Python package used for generating random numbers.
- `os`: This is a built-in Python package used for interacting with the operating system.

## Running the Application

To run the application, use the following command in your terminal or command prompt:

`python finance_tracker.py`

## Command Line Arguments

Currently, the application does not support command line arguments. All interactions are done within the application after it has started.

## Using the Application

After starting the application, you can use the following methods to track your personal finance:

- `add_expense(category: str, amount: float)`: Add an expense under a specific category.
- `set_budget(category: str, amount: float)`: Set a budget for a specific category.
- `add_savings(amount: float)`: Add an amount to your savings.
- `set_savings_goal(amount: float)`: Set a savings goal.
- `check_budget()`: Check if expenses exceed the budget for each category.
- `check_savings_goal()`: Check if savings meet or exceed the savings goal.
- `save_data()`: Save the user’s data to a file.
- `load_data()`: Load the user’s data from a file.
- `giving_some_savings_advice()`: Get a random tip on saving money.
  Remember to replace `category` and `amount` with your desired values.

## Installing the Ubuntu Terminal on Windows

1. Open the Microsoft Store.
2. Search for “Ubuntu”.
3. Select the version you want (usually the one with the highest number, which is the latest version).
4. Click “Get” or “Install”.
5. Once installed, you can launch the Ubuntu terminal from the Start menu.

## Installing Visual Studio Code

1. Go to the [VSCode download page](https://code.visualstudio.com/).
2. Download the version appropriate for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the prompts.

## Using Visual Studio Code

1. Open VSCode.
2. You can open a file or folder to work on from the “File” menu.
3. The left sidebar gives you access to the explorer (where you can see your files), source control, debugging, and extensions.
4. You can run Python code directly in VSCode by right-clicking in the file and selecting “Run Python File in Terminal”.
