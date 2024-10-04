from color_pair import get_color_from_pair_number, get_pair_number_from_color
from color_data import MAJOR_COLORS, MINOR_COLORS
import io, sys
def test_number_to_pair():
    for pair_number in range(1, 26):
        assert get_color_from_pair_number(pair_number) == get_color_from_pair_number(pair_number)
def test_pair_to_number():
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            assert get_pair_number_from_color(major_color, minor_color) == \
                   get_pair_number_from_color(major_color, minor_color)
def test_exceptions():
    assert_exception(lambda: get_color_from_pair_number(26), 'Major index out of range')
    assert_exception(lambda: get_pair_number_from_color('Invalid', 'Blue'), 'Major index out of range')
def assert_exception(func, expected_message):
    try: func()
    except Exception as e: assert str(e) == expected_message
def run_tests():
    test_number_to_pair()
    test_pair_to_number()
    test_exceptions()
if __name__ == '__main__':
    run_tests()
