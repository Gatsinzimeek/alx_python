output = ""
for n in range(100):
    if n < 10:
        output += f"0{n},"
    else:
        output += f"{n},"

print(output.rstrip(","))
