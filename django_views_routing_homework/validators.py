def validate_min_length_full_name(value):
    if len(set(value)) < 5:
        return False
    else: 
        return True
    