class Personal_Finance_Tracker:
    """
    A class to represent a personal finance tracker.

    Attributes:
    - expenses (dict): A dictionary to store expenses, where keys are expense categories and values are amounts.
    - budgets (dict): A dictionary to store budgets, where keys are budget categories and values are amounts.
    - savings (float): The total amount of savings.
    - savings_goal (float): The savings goal to be achieved.
    """

    def __init__(self):
        """
        Initializes a Personal_Finance_Tracker object with empty expenses, budgets, savings, and savings_goal.
        """
        self.expenses = {}
        self.budgets = {}
        self.savings = 0
        self.savings_goal = 0

    def add_expense(self, category, amount):
        """
        Add an expense to the tracker.

        Args:
        - category (str): The category of the expense.
        - amount (float): The amount of the expense.

        Returns:
        None
        """
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)

    def set_budget(self, category, amount):
        """
        Set a budget for a category.

        Args:
        - category (str): The category for which to set the budget.
        - amount (float): The budget amount.

        Returns:
        None
        """
        self.budgets[category] = amount

    def add_savings(self, amount):
        """
        Add savings to the tracker.

        Args:
        - amount (float): The amount of savings.

        Returns:
        None
        """
        self.savings += amount

    def set_savings_goal(self, amount):
        """
        Set the savings goal.

        Args:
        - amount (float): The savings goal.

        Returns:
        None
        """
        self.savings_goal = amount

    def check_budget(self):
        for category, budget in self.budget.items():
            if sum(self.expenses.get(category, [])) > budget:
                print(f"You have exceeded your budget for {category}.")
                
    
    def check_savings_goal(self):
        if self.savings >= self.savings_goal:
            print(f"You have reached your savings goal of ${self.savings_goal}.")
        else:
            print(f"You are {self.savings_goal - self.savings} away from your savings goal")
