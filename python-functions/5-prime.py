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

print(is_prime(17))
print(is_prime(15))
print(is_prime(4))
print(is_prime(0))

    