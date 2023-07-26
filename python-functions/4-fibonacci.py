def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_number = [0,1]
    for _ in range(2, n):
        nextNumber = fibonacci_number[-1] + fibonacci_number[-2]
        fibonacci_number.append(nextNumber)

    return fibonacci_number

