"""VB: Make it a habbit to always name your class based test files with the class name.
Eg: test_circle.py"""

import pytest
import math
from source import shapes

class TestCircle:
    
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)
        
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
    def test_perimeter(self):
        actual = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert actual == expected