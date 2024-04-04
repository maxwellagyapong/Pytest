import pytest
import time
from source import my_functions

"""How to write basic tests"""

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5  
    
def test_add_strings():
    result = my_functions.add("I like", " burgers")
    assert result == "I like burgers" 
  
def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2


# Wrong way to test an error    
# def test_divide_by_zero():
#     result = my_functions.divide(4, 0)
#     assert True

# Right way to test an error
# However it is good to handle errors in your code. This is only for learning purposes.
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(4, 0)
        

# Now lets look at pytest mark and pytest parameterize
# They allow us to add metadata to our tests
# 1. Mark
# There are a number of marks that can be added. Eg: slow, skip, xfail etc
# It allows us to condition our tests execution
# A. slow tag: tells pytest that this is a slow test
@pytest.mark.slow # Now we have add a slow tag to tell pytest that this is a slow test
def test_very_slow():
    time.sleep(5) # We intentionally do this to slow the test down
    result = my_functions.divide(10, 5)
    assert result == 2
# Adding the tags allow us to run specific groups of tests. For example we can 
# run on slow tests

# B. skip tag: Allows us to skip tests
# We can add a reason to tell other developers why we skiped that specific test 
@pytest.mark.skip(reason="This feature is broken")     
def test_add():
    assert my_functions.add(1, 2) == 3

# C. xfail: Allows a failing test to be accepted even when it fails  
@pytest.mark.xfail(reason="We know we can't divide by zero")  
def test_divide_zero_broken():
    result = my_functions.divide(4, 0)
    assert result == 2
    
# We look at parameterized in the test_square.py file