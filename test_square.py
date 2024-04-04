import pytest
import source.shapes as shapes

# Parameterized: Allows us to pass multiple values for one test without using a for loop

@pytest.mark.parametrize('side_length, expected_area', [(5, 25), (4, 16), (9, 81), (3, 9)])
def test_multiple_squares_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area
    
# In the above test, we are able to pass multiple values for one test without using
# a for loop because of the use of parameterize. We pass the multiple values pair of
# side_lengths and the corresponding areas as tuples.

@pytest.mark.parametrize('side_length, expected_perimeter', [(5, 20), (4, 16), (9, 36), (3, 12)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
    

# Now we treat mocking in the next section. 
# We create a service.py file and test_service.py file to treat mocking.