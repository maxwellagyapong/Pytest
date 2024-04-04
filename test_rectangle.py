import pytest
import source.shapes as shapes

"""Here we introduce the idea of fixtures"""

# def test_area():
#     # We create a rectangle so we can test the area
#     rectangle = shapes.Rectangle(10, 20)
#     assert rectangle.area() == 10*20
    
# def test_perimeter():
#     # We create a rectangle here again so we can test the area
#     rectangle = shapes.Rectangle(10, 20)
#     assert rectangle.perimeter() == 2*(10 + 20)
    
    
# You realize in the above tests, both test_area and test_perimeter, we create a rectangle.
# This is redundancy. We can create a single rectangle with a fixture and make use
# of that rectangle in both tests.
# Using fixture
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20
    
def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)

# You can also make use of two or more fixtures
@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)

# You can also assert two or more fixtures
def test_not_equal():
    assert my_rectangle != weird_rectangle
    
# Using fixtures from conftest.py
def test_not_equal_2(my_rect, weird_rect):
    assert my_rect != weird_rect


    