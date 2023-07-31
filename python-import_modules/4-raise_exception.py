def raise_exception():
    try:
        return("Exception has been raised")
    except TypeError as te:
        return (te)

raise_exception()
