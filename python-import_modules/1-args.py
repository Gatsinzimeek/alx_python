import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(num_arguments))
        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")
