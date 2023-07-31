import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(num_arguments))
    for i, arg in enumerate(arguments, 1):
        print(f"{i}: {arg}")
