
def collatz_sequence(start):
    """ This function creates collatz series"""
    while start > 1:
        print(int(start), end=", ")
        if start % 2 == 0:
            start = start / 2
        else:
            start = (start * 3) + 1
    print(int(start), end=".\n")


collatz_sequence(10)
