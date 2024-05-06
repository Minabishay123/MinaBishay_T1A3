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
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)

    def set_budget(self, category, amount):
        set.budget[category] = amount
