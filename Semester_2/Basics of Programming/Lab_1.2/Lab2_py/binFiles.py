def inputData(act):
    if act==0:                              #Якщо обрано очищення файлу
        with open("input.bin","wb"):
            pass
    aMins=readAndTranslate("input.bin")     #Отримуємо масив уже введених перерв
    tMins=[0,0]
    pos=0
    print("введення відбувається у форматі ГГ:ХХ")
    time=input("початок (stop для заверешення роботи): ")
    with open("input.bin","ab") as inFile:
        while time!="stop":
            h,m=-1,-1
            if time[:2].isdigit() and time[3:].isdigit():       #Перевірка на коректність
                h,m=int(time[:2]),int(time[3:])
            if time[2]!=":" or h<0 or h>23 or m<0 or m>59:
                print("Некоректний ввід. Неправильний формат даних.")
                if pos==1:
                    print("Початок перерви не дійсний")
                    pos=0
            elif pos==0:                                        #Якщо  коректно, додаємо у проміжковий масив перерви
                tMins[0]=h*60+m
                pos=1
            elif h*60+m>tMins[0]:
                tMins[1]=h*60+m
                pos=0
            else:
                print("Некоректний ввід. Початок перерви не дійсний.")
                pos=0
            inc=0
            if tMins[0]==0 or tMins[1]==0:
                inc=1
            for i in range(0, len(aMins), 2):
                if inc==0 and (tMins[0]>=aMins[i] and tMins[0]<aMins[i+1] or tMins[1]>aMins[i] and tMins[1]<=aMins[i+1] or tMins[0]<=aMins[i] and tMins[1]>=aMins[i+1]):
                    print("Перерва накладається на існуючу")
                    inc=1
            if inc==0:                                          #Не накладається - додаємо у сталий масив перерв
                aMins.append(tMins[0])
                aMins.append(tMins[1])
                inFile.write(bytes(str(tMins[0])+" "+str(tMins[1])+" ", encoding="utf-8"))
            if pos==0:
                tMins=[0,0]
                time=input("початок (stop для заверешення роботи): ")
            else:
                time=input("кінець (stop для заверешення роботи): ")

def readAndTranslate(name):
    with open(name,"rb") as inFile:                                 
        arrMins=[int(i) for i in inFile.read().split()]   #Отримуємо масив перерв
    print("Вміст файлу:")
    m=0
    for i in arrMins:
        print(str(i//60)+":"+str(i-(i//60)*60), end=" ")
        if m==0:
            print("- ", end="")
            m=1
        else:
            m=0
    print()
    return arrMins

def verify(n, name):
    time=24*60
    aMins=readAndTranslate(name)
    for i in range(0, len(aMins), 2):                               #Віднімаємо від усього часу час кожної з перерв
        time-=(aMins[i+1]-aMins[i])
    print("Ви маєте в запасі", time, "хвилин.")
    print("На", n, "клієнтів знадобиться", n*15, "хвилин.")
    time-=n*15                                                      #Розрахунок 15 хв на клієнта
    if time<0:
        print("Часу недостатньо")
    else:
        print("Часу достатньо")