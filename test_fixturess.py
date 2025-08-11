import pytest
from fixturess import usermanager

@pytest.fixture
def user_manager():
    "Creates a fresh instance of Usermanager everytime before running each code snippet in isolation"
    return usermanager()

#Basically Line 4-7 if commented out will give a duplicate value if we manually create a variable, since if we make a user_manager variable globally, the first funcion value will be assigned to it and become duplicate.
#user_manager = usermanager() would give duplicate.

    
def test_add_user(user_manager):
    assert user_manager.add_user("John", "john@gmail.com") == True
    assert user_manager.get_user("John") ==  "john@gmail.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("John", "john@gmail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("John", "another@example.com")
    