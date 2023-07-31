import sys


if __name__ == "__main__":
    arguments = sys.argv[1:] 

    num_arguments = len(arguments)
    plural = 's' if num_arguments != 1 else ''
    print(f"Number of argument{plural}: {num_arguments}:")
    if num_arguments > 0:
        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")
