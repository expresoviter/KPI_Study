from classlab import *
from funclab import *
from random import randint

n=int(input("Введіть кількість об'єктів: "))
arr=[Func(randint(0,20), randint(0,20)) for i in range(n)]
allPrint(arr)
x=int(input("\nВведіть x: "))
m, ind=maxValue(arr,x)
print("Найбльше значення",m,"у точці x =",x, "приймає функція ", end="")
print(arr[ind].getFunc())

