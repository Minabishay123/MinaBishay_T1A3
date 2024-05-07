import pytest
from finance_tracker import Personal_Finance_Tracker

def test_add_expense():
    """
    Test the add_expense method of the Personal_Finance_Tracker class.

    This test checks if the add_expense method raises a ValueError when trying to add a negative expense.
    """
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.add_expense("food", -50)

def test_set_budget():
    """
    Test the set_budget method of the Personal_Finance_Tracker class.

    This test checks if the set_budget method raises a ValueError when trying to set a negative budget.
    """
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.set_budget("food", -200)

def test_add_savings():
    """
    Test the add_savings method of the Personal_Finance_Tracker class.

    This test checks if the add_savings method raises a ValueError when trying to add a negative savings amount.
    """
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.add_savings(-900)

def test_set_savings_goal():
    """
    Test the set_savings_goal method of the Personal_Finance_Tracker class.

    This test checks if the set_savings_goal method raises a ValueError when trying to set a negative savings goal.
    """
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.set_savings_goal(-600)
