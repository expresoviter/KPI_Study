n=int(input("Введіть кількість членів n: ")) 
a=2 #Ініціалізуємо змінну члена послідовности, яка спершу дорівнює першому члену
s=2 #Ініціалізуємо змінну суми 
for i in range(n-1): #Оскільки перший член уже існує, то потрібно порахувати ще (n-1) членів
    a=(a**2)/(a+3) #Шукаємо наступний член за формулою і переприсвоюємо значення змінної члена
    s+=a #Додаємо член послідовности до суми
print("Сума елементів послідовности =",s)
 
