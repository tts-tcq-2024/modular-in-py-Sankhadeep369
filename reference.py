from color_pair import get_color_from_pair_number, color_pair_to_string

def generate_reference_manual():
    """Generates a reference manual of color pairs."""
    manual = []
    for pair_number in range(1, 26):
        major, minor = get_color_from_pair_number(pair_number)
        manual.append(f'{pair_number}: {color_pair_to_string(major, minor)}')
    return "\n".join(manual)
