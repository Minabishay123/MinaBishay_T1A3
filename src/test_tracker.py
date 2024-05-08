import pytest
from unittest.mock import patch
from finance_tracker import Personal_Finance_Tracker

def test_add_expense():
    """
    Test the add_expense method of the Personal_Finance_Tracker class.

    This test checks if the add_expense method raises a ValueError when trying to add a negative expense.
    """
    tracker = Personal_Finance_Tracker()
    with patch('builtins.input', side_effect=["food", "-50", "done"]):
        with pytest.raises(ValueError):
            tracker.add_expense()

def test_set_budget():
    """
    Test the set_budget method of the Personal_Finance_Tracker class.

    This test checks if the set_budget method raises a ValueError when trying to set a negative budget.
    """
    tracker = Personal_Finance_Tracker()
    with patch('builtins.input', side_effect=["food", "-200"]):
        with pytest.raises(ValueError):
            tracker.set_budget()

def test_add_savings():
    """
    Test the add_savings method of the Personal_Finance_Tracker class.

    This test checks if the add_savings method raises a ValueError when trying to add a negative savings amount.
    """
    tracker = Personal_Finance_Tracker()
    with patch('builtins.input', side_effect=["-900"]):
        with pytest.raises(ValueError):
            tracker.add_savings()

def test_set_savings_goal():
    """
    Test the set_savings_goal method of the Personal_Finance_Tracker class.

    This test checks if the set_savings_goal method raises a ValueError when trying to set a negative savings goal.
    """
    tracker = Personal_Finance_Tracker()
    with patch('builtins.input', side_effect=["-600"]):
        with pytest.raises(ValueError):
            tracker.set_savings_goal()
