from math import sin
class Func:
    """Функція sin(a*x+b)"""
    def __init__(self, A, B):
        self.a=A
        self.b=B
    def getValue(self,x):
        return sin(self.a*x+self.b)
    def getFunc(self):
        return "sin("+str(self.a)+"x+"+str(self.b)+")"

