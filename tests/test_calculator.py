from hamcrest import assert_that, equal_to
from src.calculator import add

def test_adds_two_numbers():
    assert_that(add(1, 2), equal_to(3))
