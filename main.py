
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

# color_utils.py

from color_constants import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
    """Returns a formatted string for the color pair."""
    return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
    """Returns the color pair for the given pair number."""
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise ValueError('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise ValueError('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    """Returns the pair number for the given color pair."""
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise ValueError('Major index out of range')
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise ValueError('Minor index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1

def print_color_code_reference():
    """Prints the color coding manual in a readable format."""
    manual = []
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual.append(f'{pair_number}: {major_color} - {minor_color}')
    return '\n'.join(manual)

# test_color_code.py

from color_utils import get_color_from_pair_number, get_pair_number_from_color

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed!')
