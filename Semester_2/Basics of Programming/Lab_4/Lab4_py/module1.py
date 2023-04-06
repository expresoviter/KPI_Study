from random import randint

class TIntNumber:
    def __init__(self,number,base):
        if base<=16:
            self.number=str(number)
            self.base=base
        else:
            print("Основа > 16, задання за замовчуванням числа 73а у 16-ій системі.")
            self.number="73a"
            self.base=16

    def getValue(self):
        print(self.number,end=" ")
        return self.number

    def toBase(self,newBase):							#Перевід між системами
	    dt=["a",11,"b",12,"c",13,"d",14,"e",15]
	    dec=0
	    for i in range(len(self.number)):
		    if self.number[i] in dt:
			    s=dt[dt.index(self.number[i])+1]
		    else:
			    s=self.number[i]
		    dec+=int(s)*(self.base)**(len(self.number)-i-1)
	    bt=""
	    if dec==0:
		    return TIntNumber("0",newBase)
	    while dec!=0:
		    if dec%newBase in dt:
			    bt+=dt[dt.index(dec%newBase)-1]
		    else:
			    bt+=str(dec%newBase)
		    dec//=newBase
	    bt=bt[::-1]
	    return TIntNumber(bt,newBase)

    def compare(self,obj):								#Порівняння у загальному випадку
	    n1,n2=self.toBase(10),obj.toBase(10)
	    if int(n1.number)>int(n2.number):
		    print(self.number,"у",self.base,"-ій системі >",obj.number,"у",obj.base,"-ій системі")
		    return self
	    elif int(n1.number)==int(n2.number):
		    print(self.number,"у",self.base,"-ій системі =",obj.number,"у",obj.base,"-ій системі")
		    return self
	    else:
		    print(self.number,"у",self.base,"-ій системі <",obj.number,"у",obj.base,"-ій системі")
		    return obj

    def add(self,obj):									#Додаємо між системами
	    n1,n2=self.toBase(10),obj.toBase(10)
	    n1.number=str(int(n1.number)+int(n2.number))
	    self.number=(n1.toBase(self.base)).number

class TIntNumber2(TIntNumber):
	def __init__(self,number):
		number=str(number)
		if number.count("0")+number.count("1")==len(number):
			self.number=number
		else:
			print("Не двійкове число, задання за замовчуванням 110.")
			self.number="110"
		self.base=2
	def compare(self,obj):								#Порівняння у двійковій - стандартно
	    print("\nУ двійковій - порівнюємо TIntNumber2`s")
	    if int(self.number)>int(obj.number):
                print("Сума вісімкових чисел менша")
	    elif int(self.number)==int(obj.number):
                print("Суми рівні")
	    else:
                print("Сума двійкових чисел менша")
	    print(max(int(self.number),int(obj.number)),">", min(int(self.number),int(obj.number)))
	    return TIntNumber2(max(int(self.number),int(obj.number)))
	def toBase(self,newBase):							#З двійкової у вісімкової - можливість тріадами
		if newBase==8:
			dt={"000":"0","001":"1","010":"2","011":"3","100":"4","101":"5","110":"6","111":"7"}
			if len(self.number)%3!=0:
				self.number="0"*(3-len(self.number)%3)+self.number
			oc=""
			for i in range(0,len(self.number),3):
				oc+=dt[self.number[i:i+3]]
			return(TIntNumber8(oc))
		else:
			return TIntNumber.toBase(self,newBase)

class TIntNumber8(TIntNumber):
	def __init__(self,number):
		number=str(number)
		if number.count("8")+number.count("9")==0:
			self.number=number
		else:
			print("Не вісімкове число, задання за замовчуванням 33.")
			self.number=33
		self.base=8
	def toBase(self,newBase):					#Тріади до двійкової
		if newBase==2:
			dt={"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
			bi=""
			for i in range(len(self.number)):
				bi+=dt[self.number[i]]
			return(TIntNumber2(bi))
		else:
			return TIntNumber.toBase(self,newBase)


def createNum(m, base):						#Створюємо необхідні числа в системі
    a=[]
    for i in range(m):
        b=""
        for j in range(randint(2,5)):
            b+=str(randint(0,base-1))
        if base==2:
            a.append(TIntNumber2(str(int(b))))
        elif base==8:
            a.append(TIntNumber8(str(int(b))))
        else:
            a.append(TIntNumber(str(int(b)),base))
    return a




