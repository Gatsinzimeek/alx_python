def raise_exception():
    try:
        print("Exception has been raised")
    except TypeError as te:
        return (te)

raise_exception()
