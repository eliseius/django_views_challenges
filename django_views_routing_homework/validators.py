def validate_min_length_full_name(value):
    return not len(set(value)) < 5
    