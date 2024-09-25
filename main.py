MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ['Blue', 'Orange', 'Green', 'Brown', 'Slate']

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
    major, minor = divmod(pair_number - 1, len(MINOR_COLORS))
    if major >= len(MAJOR_COLORS): raise ValueError('Major index out of range')
    return MAJOR_COLORS[major], MINOR_COLORS[minor]

def get_pair_number_from_color(major_color, minor_color):
    try: return MAJOR_COLORS.index(major_color) * len(MINOR_COLORS) + MINOR_COLORS.index(minor_color) + 1
    except ValueError: raise ValueError('Color index out of range')

def print_color_code_reference():
    return '\n'.join(f'{i+1}: {m} - {n}' for i, (m, n) in enumerate([(M, N) for M in MAJOR_COLORS for N in MINOR_COLORS]))

if __name__ == '__main__':
    print(print_color_code_reference())
    assert(get_color_from_pair_number(4) == ('White', 'Brown'))
    assert(get_pair_number_from_color('Black', 'Orange') == 12)
    print('Done :)')

