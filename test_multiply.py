import pytest

@pytest.mark.parametrize("num, output",[(1,10),(2,20),(3,34),(4,44), (5,66)])
def test_multiplication(num, output):
   assert 10*num == output