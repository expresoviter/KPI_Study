def isCorrect(st):
    j=0
    for i in range(len(st)):
        if ord(st[i]) < 48 and ord(st[i])!=32 or ord(st[i]) > 57:
            j=1
    return j

def minAndMax(st, cor):
    i,j=0,0
    arr=[]
    while i!=len(st) and cor==0:                        #Проходимо до кінця рядка
        if st[i]!=' ':                                  #Знаходимо перший символ після пробілу - початок числа
            temp=""
            ind=i
            while i!=len(st) and st[i]!=' ':            #Поки йдуть цифри за першою
                temp+=st[i]                             #Формуємо число в окремій змінній
                i+=1
            if j==0:                                    #Перше входження - перше число
                arr=[int(temp), ind,int(temp), ind]
                j=1
            else:
                if int(temp)<arr[0]:
                    arr[0]=int(temp)
                    arr[1]=ind
                if int(temp)>arr[2]:
                    arr[2]=int(temp)
                    arr[3]=ind
        else:
            i+=1
    return arr

def replacement(st,arr, cor):
    stOut=""
    if cor==1:
        stOut="Некоректний заданий текст"
    else:
        i=0
        while i!=len(st):
            if i==arr[1]:                                   #Індекс мінімуму - додаємо до нової змінної максимум
                stOut+=str(arr[2])
                i+=len(str(arr[0]))
            elif i==arr[3]:                                 #Індекс максимуму - додаємо мінімум
                stOut+=str(arr[0])
                i+=len(str(arr[2]))
            else:
                stOut+=st[i]
                i+=1
    return stOut

st=input("Введіть  рядок  з  цифрами  і  пробілами  : ")
cor=isCorrect(st)
arr=minAndMax(st, cor)
stOut=replacement(st,arr, cor)
print("Рядок із заміненими максимумом і мінімумом:", stOut)
