def fact(c):
    if c==0:                                    #0!=1
        return 1
    else:
        s=1                                     #Змінна факторіалу числа
        for i in range(2,c+1):                  #Знаходження факторіалу за допомогою аритметичного циклу
            s*=i
        return s                                #Повертаємо значення факторіалу
def pascal(b):
    for k in range(b+1): 
        for j in range(k+1):                    #Цикл для елементів у конкретному рядку
            o=fact(k)//(fact(k-j)*fact(j))
            print(o,end=' ')                    #Виводимо комбінацію без переходу на новий рядок
        print()
n=int(input("Введіть n: "))
pascal(n)