from module1 import *

m=int(input("Введіть кількість двійкових чисел: "))
n=int(input("Введіть кількість вісімкових чисел: "))
binArr,octArr=createNum(m,2), createNum(n,8)
sBin,sOct=TIntNumber2("0"),TIntNumber8("0")
print("\nДвійкові числа:")
for i in binArr:
    i.getValue()
    sBin.add(i)
print("\n\nВісімкові числа:")
for i in octArr:
    i.getValue()
    sOct.add(i)
print("\n\nСума двійкових чисел =",end=" ") 
sBin.getValue()
print("\nСума вісімкових чисел =",end=" ")
sOct.getValue()
s8Bin=sOct.toBase(2)
print("\n\nСума вісімкових у двійковому форматі =",end=" ")
s8Bin.getValue()
print()
sBin.compare(s8Bin)
