#!/usr/bin/python3
if __name__ == "__main__":
    import sys

count = len(sys.argv) - 1
loop_count = 0

if count == 0:

	print("0 arguments")
elif count < 2:
	print("1 argument")
else:

	print(str(count) + ": arguments")


for i in range(count):
	print("{}: {}".format(i + 1, sys.argv[i + 1]))
