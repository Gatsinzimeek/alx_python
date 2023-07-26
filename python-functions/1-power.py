def pow(a,b):
    Expon = 1
    if b==0:
        return 1
    elif b > 0:
        for _ in range(b):
            Expon *= a
        return Expon
    else:
        for _ in range(b):
            Expon *= a
        return 1/Expon
