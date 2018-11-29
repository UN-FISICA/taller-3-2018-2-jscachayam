import myfloat_func as my

class MyFloat:

    def __init__(self,t):
        if type(t)!=tuple:
            self.e=my.entero(t)[0]
            self.d=my.entero(t)[1]
        else:
            self.e=t[0]
            self.d=t[1]
        self.t=(self.e,self.d)
    
    def __add__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.suma(a,b)))

    def __sub__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.resta(a,b)))

    def __mul__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.multiplicacion(a,b)))

    def __truediv__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.division(a,b)))

    def __radd__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.suma(b,a)))

    def __rsub__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.resta(b,a)))

    def __rmul__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.multiplicacion(b,a)))

    def __rtruediv__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        return(MyFloat(my.division(b,a)))

    def __str__(self):
        return(my.imprimir(self.t))
        
    def __repr__(self):
        return(my.imprimir(self.t))

    def __eq__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        if my.resta(a,b)==([0,'+'],[0]):
            return True
        else:
            return False

    def __ne__(self,other):
        E1=self.e[::]
        D1=self.d[::]
        if type(other)==MyFloat:    
            E2=other.e[::]
            D2=other.d[::]
        elif type(other)==tuple:
            E2=other[0][::]
            D2=other[1][::]
        else:
            E2=my.entero(other)[0]
            D2=my.entero(other)[1]
        a=(E1,D1)
        b=(E2,D2)
        if my.resta(a,b)==([0,'+'],[0]):
            return False
        else:
            return True

if __name__ == "__main__":
    x=MyFloat(0)
    for k in range(5000000):
        if k%2!=0:
            num=-4
        else:
            num=4
        dem=MyFloat(2)*my.entero(k) + 1
        div=num/dem
        x=x+div
    print(x)
