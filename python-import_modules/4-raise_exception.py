def raise_exception():
    try:
        raise TypeError("This is a type exception!")
    except TypeError as e:
        print("An exception occurred:", e)

raise_exception()