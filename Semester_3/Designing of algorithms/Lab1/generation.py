from random import randint


def generation():
    n = float(input("Size of the file (MB): "))
    with open("A.txt", "w") as a:
        size = 0
        while size < 1048576 * (n+1):
            tmp = str(randint(0, 99999999)) + "\n"
            size += len(tmp) + 1
            a.write(tmp)
