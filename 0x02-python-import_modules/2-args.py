#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(i, "" if i == 1 else "s", "." if i == 0 else ":"))
    for i in range(l):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
