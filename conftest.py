"""Alternatively, you can create this conftest.py file and create all your fixtures there.
This is an example"""

import pytest
import source.shapes as shapes

@pytest.fixture
def my_rect():
    return shapes.Rectangle(10, 35)

@pytest.fixture
def weird_rect():
    return shapes.Rectangle(5, 7)

# You can directly make use of all fixtures created in this file in any of your test_files
# without having to import 