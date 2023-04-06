def splitF():
    a = open("A.txt")
    b, c = open("B.txt", "w"), open("C.txt", "w")
    cur = []
    p = 1
    for line in a:
        if cur == [] or int(line.split()[0]) >= int(cur[-1]):
            cur += line.split()
        else:
            if p == 1:
                b.write(" ".join(cur) + "\n")
                p = 2
            else:
                c.write(" ".join(cur) + "\n")
                p = 1
            cur = line.split()
    if p == 1:
        b.write(" ".join(cur))
    else:
        c.write(" ".join(cur))
    a.close()
    b.close()
    c.close()
    mergeF()


def mergeF():
    a = open("A.txt", "w")
    b, c = open("B.txt"), open("C.txt")
    if len(b.readlines()) < len(c.readlines()):
        b.close()
        c.close()
        c, b = open("B.txt"), open("C.txt")
    b.seek(0)
    c.seek(0)
    for lineb in b:
        lc = [int(i) for i in c.readline().split()]
        lb = [int(i) for i in lineb.split()]
        la, i, j = [], 0, 0
        while i != len(lb) and j != len(lc):
            if lb[i] < lc[j]:
                la.append(lb[i])
                i += 1
            else:
                la.append(lc[j])
                j += 1
        while i != len(lb):
            la.append(lb[i])
            i += 1
        while j != len(lc):
            la.append(lc[j])
            j += 1
        a.write(" ".join([str(i) for i in la]) + "\n")
    for linec in c:
        a.write(linec)
    a.close()
    b.close()
    c.close()
    with open("A.txt") as a:
        if len(a.readlines()) != 1:
            splitF()
