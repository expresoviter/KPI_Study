import msvcrt

def processLine(lines):
    coun=0
    for i in range(len(lines)):
        lines[i]=lines[i].split()
        lineTemp=""
        for k in lines[i]:
            if len(k)==2:                       #Враховуємо двосимвольні слова
                coun+=1
                print(k,end=" ")
            else:
                lineTemp+=k
                lineTemp+=" "
        lines[i]=lineTemp
    outText="\n".join(lines)
    return outText, coun

def output(name):
    with open(name) as file:
        for i in file.readlines():
            print(i, end="")

def enter(act):
    if act==0:                                  #Якщо задано очищення вхідного файлу
        with open("input.txt","w") as inFile:
            pass
    with open("input.txt","a") as inFile:
        print("Enter lines (`shift+e` to finish entering).")
        m = msvcrt.getch().decode('ASCII')
        while m!='E':                           #Перевіряємо, чи введений shift+e 
            print(m,end="")
            inp=input()
            inFile.write(m+inp+"\n")
            m = msvcrt.getch().decode('ASCII')

def writing(inName,outName):
    with open(inName,"r") as inFile:
        with open(outName,"w") as outFile:
            outFile.write("")
        with open(outName,"a") as outFile:
            print("\nRemoved words: ", end="")
            line=inFile.readlines()
            lineOut, coun=processLine(line)     #Оброблюємо текст відповідно до умови
            print()
            outFile.write(lineOut)
            outFile.write("\nAmount of removed words = "+str(coun)+"\n")


