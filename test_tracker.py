import pytest
from finance_tracker import Personal_Finance_Tracker

def test_add_expense():
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.add_expense("food", -50)
      
        
def test_set_budget():
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.set_budget("food", -200)
     
        

def test_add_savings():
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.add_savings(-900)
        

def test_set_savings_goal():
    tracker = Personal_Finance_Tracker()
    with pytest.raises(ValueError):
        tracker.set_savings_goal(-600)