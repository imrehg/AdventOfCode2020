import pytest
from day05 import seat_decode


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_decode(test_input, expected):
    assert seat_decode(test_input) == expected
