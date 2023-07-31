def raise_exception():
    try:
        print("Exception raised")
    except TypeError as e:
        return (e)

raise_exception()
