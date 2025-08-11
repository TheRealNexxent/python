import pytest
from db import Database

@pytest.fixture
def db():
    "Fresh instance of db and clears it after"
    database = Database()
    yield database #Means, it will yield the data till here, and run the whole command for the test, and then whatever comes below this line will run after completion of the test so every database is clean and new.
    database.data.clear()

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_dup_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match = "Already exists"):
        db.add_user(1, "Bob")

def test_del_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None