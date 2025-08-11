from pytestt2 import add, divide
import pytest

def test_add():
    assert add(2,3) == 5, "2+3 should be 5" #Optional comment to show what its sposed to do
    assert add(3,5) == 8, "3+5 should be 8"
    assert add(0,0) == 0, "0+0 should be 0"

def test_divide():
    with pytest.raises(ValueError, match = "Cannot divide by Zero!"):
        divide(10,0)

def test_divide():
    assert divide(2,1) == 2, "2/1 should be 2"
    assert divide(2,2) == 1, "2/2 should be 1"

#Test all edge cases! Type errors etc