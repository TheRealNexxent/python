from pytestt import get_weather

def test_get_weather():
    assert get_weather(21) == "Hot"
    assert get_weather(100) == "Hot"
    assert get_weather(0) == "Cold"

#Assertion tells us if something is true or false.
#If true: Testcase Passed, else Failed.
#NOTE: the reason why we put test_get_weather instead of get_weather is because test should come fist in the function name in order fot pytest to read it and test it. Dont type get_test_weather either, wont work!


#Unit tests are smallest tests, of components of code. Limited functions. Its to ensure you get expected output from small code snippet. To cover majority of code
#Integration Test, System Test, etc are also used.

#Useful to isolate that small funcitons are working fine, and its something bigger.
