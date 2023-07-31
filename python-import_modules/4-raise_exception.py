def raise_exception():
    try:
        print("This is a type exception!")
    except TypeError as e:
        print("Exception has been raised:", e)

raise_exception()
