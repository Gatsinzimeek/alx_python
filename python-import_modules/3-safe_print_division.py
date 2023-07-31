def safe_print_division(a,b):
    int(a)
    int(b)
    if b == 0:
        return None
    else:
        try:
            result = a / b
            return result
        except ValueError:
            return("Invalid: please enter valid integers")
        