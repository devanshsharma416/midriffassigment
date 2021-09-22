import pytest
@pytest.mark.xfail
@pytest.mark.skip
def test_greater():
   n = 150
   assert n > 100

@pytest.mark.xfail
@pytest.mark.skip
def test_greater_equal():
   n = 50
   assert n >= 100


@pytest.mark.xfail
@pytest.mark.skip
def test_less():
   n = 100
   assert n < 200