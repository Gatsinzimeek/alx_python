def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number):
            # checking for factor
            if number % i == 0:
            # return False
                return False
        # returning True
    return True
    
