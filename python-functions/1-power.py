def pow(a,b):
    if b==0:
        return 1
    else:
        Expon = 1
        for _ in range(b):
            Expon *= a
        return Expon
