for n in range(99):
    if n < 10:
        print(f"{str(n)} = 0x{str(n)}")
    elif n < 16 and n > 9:
        print(f"{str(n)} = 0x{str(chr(n[:2] + 97))}")
    else:
        print(f"{str(n)}")
