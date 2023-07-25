def validate_password(password ):
    for i in password:
        checkCharacter = i
        if checkCharacter == 8 and password[i].isupper() == True and password[i].islower() == True:
            return True
        else:
            return False
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
