def imprimir(a):
    if type(a)=!tuple:
        return a
    a[0].reverse()
    str1 = ''.join(str(e) for e in a[0])
    str2 = ''.join(str(e) for e in a[1])
    a[0].reverse()
    str3=str1+","+str2
    return str3


def suma(a, b):
    a[0].reverse()
    b[0].reverse()
    da1 = ''.join(str(e) for e in a[1])
    db1 = ''.join(str(e) for e in b[1])
    ea1 = ''.join(str(e) for e in a[0])
    eb1 = ''.join(str(e) for e in b[0])
    if a[0][0]=="-":
        i=ea1.replace("-","") 
        ea=float(i) 
        da=float("0."+da1)
        da=da*-1
        ea=ea*-1
    else:
        i=ea1.replace("+","") 
        ea=float(i) 
        da=float("0."+da1)
        
    if b[0][0]=="-":
        i=eb1.replace("-","") 
        eb=float(i) 
        db=float("0."+db1)  
        db=db*-1
        eb=eb*-1
    else:
        i=eb1.replace("+","") 
        eb=float(i) 
        db=float("0."+db1)
        
    a[0].reverse()
    b[0].reverse()
    na=ea+da
    nb=eb+db
    nc=na+nb
    if nc>0:
        ec=int(nc)
        dc=nc-int(nc)
        E="+"+str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    else:
        ec=int(nc)
        dc=abs(nc)-abs(int(nc))
        E=str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    D.pop(0)
    D.pop(0)
    c=(E,D)
    return c
    
def resta(a, b):
    a[0].reverse()
    b[0].reverse()
    da1 = ''.join(str(e) for e in a[1])
    db1 = ''.join(str(e) for e in b[1])
    ea1 = ''.join(str(e) for e in a[0])
    eb1 = ''.join(str(e) for e in b[0])
    if a[0][0]=="-":
        i=ea1.replace("-","") 
        ea=float(i) 
        da=float("0."+da1)
        da=da*-1
        ea=ea*-1
    else:
        i=ea1.replace("+","") 
        ea=float(i) 
        da=float("0."+da1)
        
    if b[0][0]=="-":
        i=eb1.replace("-","") 
        eb=float(i) 
        db=float("0."+db1)  
        db=db*-1
        eb=eb*-1
    else:
        i=eb1.replace("+","") 
        eb=float(i) 
        db=float("0."+db1)
        
    a[0].reverse()
    b[0].reverse()
    na=ea+da
    nb=eb+db
    nc=na-nb
    if nc>0:
        ec=int(nc)
        dc=nc-int(nc)
        E="+"+str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    else:
        ec=int(nc)
        dc=abs(nc)-abs(int(nc))
        E=str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    D.pop(0)
    D.pop(0)
    c=(E,D)
    return c
   

def multiplicacion(a, b):
    a[0].reverse()
    b[0].reverse()
    da1 = ''.join(str(e) for e in a[1])
    db1 = ''.join(str(e) for e in b[1])
    ea1 = ''.join(str(e) for e in a[0])
    eb1 = ''.join(str(e) for e in b[0])
    if a[0][0]=="-":
        i=ea1.replace("-","") 
        ea=float(i) 
        da=float("0."+da1)
        da=da*-1
        ea=ea*-1
    else:
        i=ea1.replace("+","") 
        ea=float(i) 
        da=float("0."+da1)
        
    if b[0][0]=="-":
        i=eb1.replace("-","") 
        eb=float(i) 
        db=float("0."+db1)  
        db=db*-1
        eb=eb*-1
    else:
        i=eb1.replace("+","") 
        eb=float(i) 
        db=float("0."+db1)
        
    a[0].reverse()
    b[0].reverse()
    na=ea+da
    nb=eb+db
    nc=na*nb
    if nc>0:
        ec=int(nc)
        dc=nc-int(nc)
        E="+"+str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    else:
        ec=int(nc)
        dc=abs(nc)-abs(int(nc))
        E=str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    D.pop(0)
    D.pop(0)
    c=(E,D)
    return c
   
def division(a, b):
    a[0].reverse()
    b[0].reverse()
    da1 = ''.join(str(e) for e in a[1])
    db1 = ''.join(str(e) for e in b[1])
    ea1 = ''.join(str(e) for e in a[0])
    eb1 = ''.join(str(e) for e in b[0])
    if a[0][0]=="-":
        i=ea1.replace("-","") 
        ea=float(i) 
        da=float("0."+da1)
        da=da*-1
        ea=ea*-1
    else:
        i=ea1.replace("+","") 
        ea=float(i) 
        da=float("0."+da1)
        
    if b[0][0]=="-":
        i=eb1.replace("-","") 
        eb=float(i) 
        db=float("0."+db1)  
        db=db*-1
        eb=eb*-1
    else:
        i=eb1.replace("+","") 
        eb=float(i) 
        db=float("0."+db1)
        
    a[0].reverse()
    b[0].reverse()
    na=ea+da
    nb=eb+db
    nc=na/nb
    if nc>0:
        ec=int(nc)
        dc=nc-int(nc)
        E="+"+str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    else:
        ec=int(nc)
        dc=abs(nc)-abs(int(nc))
        E=str(ec)
        D=str(dc)
        E=list(E)
        D=list(D)
    D.pop(0)
    D.pop(0)
    c=(E,D)
    return c

def comparacion(a, b):
    a[0].reverse()
    b[0].reverse()
    da1 = ''.join(str(e) for e in a[1])
    db1 = ''.join(str(e) for e in b[1])
    ea1 = ''.join(str(e) for e in a[0])
    eb1 = ''.join(str(e) for e in b[0])
    if a[0][0]=="-":
        i=ea1.replace("-","") 
        ea=float(i) 
        da=float("0."+da1)
        da=da*-1
        ea=ea*-1
    else:
        i=ea1.replace("+","") 
        ea=float(i) 
        da=float("0."+da1)
        
    if b[0][0]=="-":
        i=eb1.replace("-","") 
        eb=float(i) 
        db=float("0."+db1)  
        db=db*-1
        eb=eb*-1
    else:
        i=eb1.replace("+","") 
        eb=float(i) 
        db=float("0."+db1)
        
    a[0].reverse()
    b[0].reverse()
    na=ea+da
    nb=eb+db
    if na==nb:
        print("las tuplas representan el mismo numero")
    else:
        print("las tuplas representan numeros diferentes")

def pi(n):
    pi=0
    for k in range(n+1):
        pi += 2 * (-1)**k * 3**(1/2 - k) / (2 * k + 1)
    return pi


if __name__ == "__main__":
