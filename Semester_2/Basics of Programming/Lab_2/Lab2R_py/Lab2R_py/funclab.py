def maxValue(arr,x):
    m=-10
    for i in range(len(arr)):
        if arr[i].getValue(x)>m:
            m=arr[i].getValue(x)
            ind=i
    return m,ind

def allPrint(arr):
    print("Створені об'єкти:")
    for i in arr:
        print(i.getFunc())

