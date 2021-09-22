import pytest
@pytest.fixture
def given_value():
   num = 39
   return num

def test_divisible(given_value):
   assert given_value % 3 == 0

def test_multiply(input_value):
   assert given_value * 6 == 100

def test_add(input_value):
   assert given_value + 60 == 99