def reading(filename):
    with open(filename, "r") as inFile:
        u, m=map(int, inFile.readline().split())
        d=[]
        for i in range(u):
            d.append([int(j) for j in inFile.readline().split()])
    return u,m,d

def allDataInv(u,m,x,d):
    b, bRev=[0 for i in range(m)], [0 for i in range(m)]    #списки віддалення уподобань глядача 1 від глядача 2 і навпаки
    invArr=[]
    for i in range(u):
        if d[i][0]==x:
            ix=i
    for i in range(u):
        if d[i][0]!=x:
            for j in range(1,m+1):
                b[d[ix][j]-1]=d[i][j]           
                bRev[d[i][j]-1]=d[ix][j]
            sArr,c=countInv(b)
            sArrRev,cRev=countInv(bRev)
            if c==cRev:                                     #переконуємося, що кількість інверсій в обох випадках незмінна
                invArr.append([d[i][0],c])
    return invArr

def countInv(a):
    if len(a)==1:
        return a, 0
    else:
        l, x=countInv(a[:len(a)//2])
        r, y=countInv(a[len(a)//2:])
        a, z=countSplitInv(a, l, r)
        return a,x+y+z

def countSplitInv(a,l,r):
    l.append(max(a)*2)
    r.append(max(a)*2)
    i,j,c=0,0,0
    for k in range(len(a)):
        if l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
            c+=(len(l)-i-1)
    return a,c

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j + 1][1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def writing(x, filename, invArr):
    with open(filename,"w") as outFile:
        outFile.write(str(x)+"\n")
        for i in range(len(invArr)):
            outFile.write(str(invArr[i][0])+" "+str(invArr[i][1])+"\n")

u,m,d=reading("input_02.txt")
x=int(input("x = "))
invArr=allDataInv(u,m,x,d)
bubbleSort(invArr)
writing(x, "ip11_lesiv_02_output.txt", invArr)
