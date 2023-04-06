from random import randint
from datetime import datetime
def bubbleSort(arr):
    swaps, comparations=0,0
    start=datetime.now()
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            comparations+=1
            if arr[j]<arr[j+1]:
                swaps+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
    time=datetime.now()-start
    return arr, comparations, swaps, time

def combSort(arr):
    swaps, comparations=0,0
    gap=len(arr)
    swapped=True
    start=datetime.now()
    while gap>1 or swapped:
        gap=max(1,int(gap/1.24733))
        swapped=False
        for i in range(len(arr)-gap):
            comparations+=1
            if arr[i]<arr[i+gap]:
                swaps+=1
                arr[i],arr[i+gap]=arr[i+gap],arr[i]
                swapped=True
    time=datetime.now()-start
    return arr, comparations, swaps, time

def cases(n):
    best=[i for i in range(n)]
    worst=[i for i in range(n,0,-1)]
    rand=[randint(0,n*2) for i in range(n)]
    return best,worst,rand

n=int(input("Введіть кількість елементів масиву: "))
bb, bw, br=cases(n)
cb, cw, cr =bb[:], bw[:], br[:]
for i in range(3):
    if i==0:
        print("Найкращий випадок:")
        b,c=bb,cb
    elif i==1:
        print("\nНайгірший випадок:")
        b,c=bw,cw
    else:
        print("\nВипадковий випадок:")
        b,c=br,cr
    arr, compBub, swapBub, timeB=bubbleSort(b)
    print("Сорт бульбашкою", arr)
    print("Сортування бульбашкою: порівнянь -",compBub, ", перестановок -",swapBub, ", час сортування -", timeB)
    arr,compComb, swapComb, timeC=combSort(c)
    print("Combsort ", arr)
    print("Сортування гребінцем: порівнянь -",compComb, ", перестановок -",swapComb, ", час сортування -", timeC)
