import sys

if __name__ == "__main__":
    count = 0

    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv)))
        for i in sys.argv:
            count += 1
            print("{}: {}".format(count,i))
