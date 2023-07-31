def raise_exception():
    try:
        print("This is a type exception!")
    except TypeError as e:
        print("An exception occurred:", e)

raise_exception()
