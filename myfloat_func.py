def imprimir(a):
    if type(a)=!tuple:
        return a
    a[0].reverse()
    str1 = ''.join(str(e) for e in a[0])
    str2 = ''.join(str(e) for e in a[1])
    a[0].reverse()
    str3=str1+","+str2
    return str3


def suma(a,b):
    #Hace copia de tuplas para trabajar con ellas
    E1=a[0][::-1]
    D1=a[1][::]
    E2=b[0][::-1]
    D2=b[1][::]
    num1=(E1,D1)
    num2=(E2,D2)
    #Iguala el tamaño de las tuplas
    if len(E1)>len(E2):
        ss=len(E1)-len(E2)    
        for i in range(ss):
            num2[0].insert(1,0)    
    elif len(E1)<len(E2):
        ss=len(E2)-len(E1)    
        for i in range(ss):
            num1[0].insert(1,0)    
    if len(D1)>len(D2):
        ss=len(D1)-len(D2)    
        for i in range(ss):
            num2[1].insert(len(D2),0)    
    elif len(D1)<len(D2):
        ss=len(D2)-len(D1)    
        for i in range(ss):
            num1[1].insert(len(D1),0)    
    #Genera tupla vacia para ser el resultado
    E3=[0]*len(E1)
    D3=[0]*len(D1)
    num3=(E3,D3)
    #evalua los casos
    if num1[0][0]==num2[0][0]:
        for i in range(len(D3)-1,-1,-1):
            num3[1][i]=num3[1][i] + num1[1][i] + num2[1][i]
            if num3[1][i]>9:
                num3[1][i]=num3[1][i]-10
                if i==0:
                    num3[0][-1]=1
                else:
                    num3[1][i-1]=1

        for i in range(len(E3)-1,-1,-1):
            if i==0:
                break
            num3[0][i]=num3[0][i] + num1[0][i] + num2[0][i]
            if num3[0][i]>9:
                if i==1:
                    num3[0][i]=num3[0][i]-10
                    num3[0].insert(1,1)
                else:
                    num3[0][i]=num3[0][i]-10
                    num3[0][i-1]=1   
        if num1[0][0]=='+':
            num3[0][0]='+'
        else:
            num3[0][0]='-'
    elif num1[0][0]!=num2[0][0]:
        m=0
        n=0
        for i in range(len(E3)-1,-1,-1):
            if i==0:
                break
            elif num1[0][i]<num2[0][i]:
                mayore=num2[0]
                menore=num1[0]
                num3[0][0]=num2[0][0]
                break
            elif num1[0][i]>num2[0][i]:
                mayore=num1[0]
                menore=num2[0]
                num3[0][0]=num1[0][0]
                break
            elif num1[0][i]==num2[0][i]:
                m=m+1
                continue
            
        for i in range(len(D3)-1,-1,-1):
            if num1[1][i]<num2[1][i]:
                mayord=num2[1]
                menord=num1[1]
                if num3[0][0]==0:
                    num3[0][0]=num1[0][0]
                break
            elif num1[1][i]>num2[1][i]:
                mayord=num1[1]
                menord=num2[1]
                if num3[0][0]==0:
                    num3[0][0]=num2[0][0]
                break
            elif num1[1][i]==num2[1][i]:
                n=n+1
                continue
        if m==len(E3)-1:
            mayore=num1[0]
            menore=num2[0]
        if n==len(D3):
            mayord=num1[1]
            menord=num2[1]
        if m==len(E3)-1 and n==len(D3):
            num3[0][0]='+'
            
        mayor=(mayore,mayord)
        menor=(menore,menord)
        for i in range(len(D3)-1,-1,-1):
             num3[1][i]=num3[1][i] + menor[1][i] - mayor[1][i] 
             if num3[1][i]>9:
                 num3[1][i]=num3[1][i]-10
                 if i==0:
                     num3[0][-1]=1
                 else:
                    num3[1][i-1]=1
             if num3[1][i]<0:
                num3[1][i]=num3[1][i]+10
                if i==0:
                    num3[0][-1]=-1
                else:
                    num3[1][i-1]=-1
        for i in range(len(E3)-1,-1,-1):
            if i==0:
                break
            num3[0][i]=num3[0][i] + mayor[0][i] - menor[0][i]
            if num3[0][i]>9:
                if i==1:
                    num3[0][i]=num3[0][i]-10
                    num3[0].insert(1,1)
                else:
                    num3[0][i]=num3[0][i]-10
                    num3[0][i-1]=1
            if num3[0][i]<0:
                num3[0][i]=num3[0][i]+10
                num3[0][i-1]=-1
    
    num3[0].reverse()
    return num3

def resta(a,b):
    #Hace copia de tuplas para trabajar con ellas
    E1=a[0][::-1]
    D1=a[1][::]
    E2=b[0][::-1]
    D2=b[1][::]
    num1=(E1,D1)
    num2=(E2,D2)
    #Iguala el tamaño de las tuplas
    if len(E1)>len(E2):
        ss=len(E1)-len(E2)    
        for i in range(ss):
            num2[0].insert(1,0)    
    elif len(E1)<len(E2):
        ss=len(E2)-len(E1)    
        for i in range(ss):
            num1[0].insert(1,0)    
    if len(D1)>len(D2):
        ss=len(D1)-len(D2)    
        for i in range(ss):
            num2[1].insert(len(D2),0)    
    elif len(D1)<len(D2):
        ss=len(D2)-len(D1)    
        for i in range(ss):
            num1[1].insert(len(D1),0)    
    #cambia signo de la tupla b 
    if num2[0][0]=='+':
        num2[0][0]='-'
    else:
        num2[0][0]='+'
    #Genera tupla vacia para ser el resultado
    E3=[0]*len(E1)
    D3=[0]*len(D1)
    num3=(E3,D3)
    #evalua los casos
    if num1[0][0]==num2[0][0]:
        for i in range(len(D3)-1,-1,-1):
            num3[1][i]=num3[1][i] + num1[1][i] + num2[1][i]
            if num3[1][i]>9:
                num3[1][i]=num3[1][i]-10
                if i==0:
                    num3[0][-1]=1
                else:
                    num3[1][i-1]=1

        for i in range(len(E3)-1,-1,-1):
            if i==0:
                break
            num3[0][i]=num3[0][i] + num1[0][i] + num2[0][i]
            if num3[0][i]>9:
                if i==1:
                    num3[0][i]=num3[0][i]-10
                    num3[0].insert(1,1)
                else:
                    num3[0][i]=num3[0][i]-10
                    num3[0][i-1]=1   
        if num1[0][0]=='+':
            num3[0][0]='+'
        else:
            num3[0][0]='-'
    elif num1[0][0]!=num2[0][0]:
        m=0
        n=0
        for i in range(len(E3)-1,-1,-1):
            if i==0:
                break
            elif num1[0][i]<num2[0][i]:
                mayore=num2[0]
                menore=num1[0]
                num3[0][0]=num2[0][0]
                break
            elif num1[0][i]>num2[0][i]:
                mayore=num1[0]
                menore=num2[0]
                num3[0][0]=num1[0][0]
                break
            elif num1[0][i]==num2[0][i]:
                m=m+1
                continue
            
        for i in range(len(D3)-1,-1,-1):
            if num1[1][i]<num2[1][i]:
                mayord=num2[1]
                menord=num1[1]
                if num3[0][0]==0:
                    num3[0][0]=num1[0][0]
                break
            elif num1[1][i]>num2[1][i]:
                mayord=num1[1]
                menord=num2[1]
                if num3[0][0]==0:
                    num3[0][0]=num2[0][0]
                break
            elif num1[1][i]==num2[1][i]:
                n=n+1
                continue
        if m==len(E3)-1:
            mayore=num1[0]
            menore=num2[0]
        if n==len(D3):
            mayord=num1[1]
            menord=num2[1]
        if m==len(E3)-1 and n==len(D3):
            num3[0][0]='+'
            
        mayor=(mayore,mayord)
        menor=(menore,menord)
        for i in range(len(D3)-1,-1,-1):
             num3[1][i]=num3[1][i] + menor[1][i] - mayor[1][i] 
             if num3[1][i]>9:
                 num3[1][i]=num3[1][i]-10
                 if i==0:
                     num3[0][-1]=1
                 else:
                    num3[1][i-1]=1
             if num3[1][i]<0:
                num3[1][i]=num3[1][i]+10
                if i==0:
                    num3[0][-1]=-1
                else:
                    num3[1][i-1]=-1
        for i in range(len(E3)-1,-1,-1):
            if i==0:
                break
            num3[0][i]=num3[0][i] + mayor[0][i] - menor[0][i]
            if num3[0][i]>9:
                if i==1:
                    num3[0][i]=num3[0][i]-10
                    num3[0].insert(1,1)
                else:
                    num3[0][i]=num3[0][i]-10
                    num3[0][i-1]=1
            if num3[0][i]<0:
                num3[0][i]=num3[0][i]+10
                num3[0][i-1]=-1
    
    num3[0].reverse()
    return num3
   

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
