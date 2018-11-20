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
 
    E1=a[0][::-1]
    D1=a[1][::]
    E2=b[0][::-1]
    D2=b[1][::]
    num1=(E1,D1)
    num2=(E2,D2)

    if len(E1)!=len(E2):
        ss=len(E1)-len(E2)    
        if ss>0:
            for i in range(ss):
                num2[0].insert(1,0)
        else:
            for i in range(ss):
                num1[0].insert(1,0) 
   
    if len(D1)!=len(D2):
        ss=len(D1)-len(D2)    
        if ss>0:
            for i in range(ss):
                num2[1].insert(len(D2),0)
        else:
            for i in range(ss):
                num1[1].insert(len(D1),0)    
   
    E3=[0]*len(E1)
    D3=[0]*len(D1)
    num3=(E3,D3)
 
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
    else:
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
    
    while num3[0][1]==0 and len(num3[0])>2:
        num3[0].pop(1)
    while num3[1][-1]==0 and len(num3[1])>1 :
        num3[1].pop(-1)

    num3[0].reverse()
    return num3

def resta(a,b):
 
    E1=a[0][::-1]
    D1=a[1][::]
    E2=b[0][::-1]
    D2=b[1][::]
    num1=(E1,D1)
    num2=(E2,D2)
    
    if num2[0][0]=='+':
        num2[0][0]='-'
    else:
        num2[0][0]='+'
        
    if len(E1)!=len(E2):
        ss=len(E1)-len(E2)    
        if ss>0:
            for i in range(ss):
                num2[0].insert(1,0)
        else:
            for i in range(ss):
                num1[0].insert(1,0) 
   
    if len(D1)!=len(D2):
        ss=len(D1)-len(D2)    
        if ss>0:
            for i in range(ss):
                num2[1].insert(len(D2),0)
        else:
            for i in range(ss):
                num1[1].insert(len(D1),0)    
   
    E3=[0]*len(E1)
    D3=[0]*len(D1)
    num3=(E3,D3)
 
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
    else:
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
    
    while num3[0][1]==0 and len(num3[0])>2:
        num3[0].pop(1)
    while num3[1][-1]==0 and len(num3[1])>1 :
        num3[1].pop(-1)

    num3[0].reverse()
    return num3
    
def multiplicacion(a,b):
    
    E1=a[0][::-1]
    D1=a[1][::]
    E2=b[0][::-1]
    D2=b[1][::]
    num1=E1+D1
    num2=E2+D2
    q=len(num1)-1
    w=len(num2)-1 
    g=[0]*w

    for k in range(w): 
        g[k]=[0]*q 
 
    for l in range(w):
        for m in range(q):
            g[l][q-m-1]= num1[q-m]*num2[w-l] + g[l][q-m-1]
            if g[l][q-m-1]>9:
                g[l][q-m-1]=str(g[l][q-m-1])
                pd=int(g[l][q-m-1][0])
                g[l][q-m-1]=int(g[l][q-m-1][1])
                if m==(q-1):
                    g[l].insert(0,pd)
                else:
                    g[l][q-m-2]=g[l][q-m-2] + pd

    for m in range(w):
        if len(g[m])==q:
            for n in range(w,m,-1):
                g[m].insert(0,0)
        else:
            for n in range(w-1,m,-1):
                g[m].insert(0,0)
    for m in range(w):
        g[m]=g[m][::-1] 
        n=0
        if n<m:
            while n<m:
                g[m].insert(0,0)
                n+=1
        g[m]=g[m][::-1]
        
    resmul=[[0]*(q+w)]
    e=len(g[0])
    for k in range(w):
        for t in range(e):
            resmul[0][e-t-1]= g[k][e-t-1] + resmul[0][e-t-1]
            if resmul[0][e-t-1]>9:
                resmul[0][e-t-1]= resmul[0][e-t-1] - 10
                g[k][e-t-2]= g[k][e-t-2] + 1
    decimal=len(a[1])+len(b[1])
    E3=resmul[0][0:(len(resmul[0])-decimal)]
    D3=resmul[0][(len(resmul[0])-decimal)::]
    num3=(E3,D3)
    
    if num2[0][0]==num1[0][0]:
        num3[0].insert(0,'+')
    else:
        num3[0].insert(0,'-')
        
    while num3[0][1]==0 and len(num3[0])>2:
        num3[0].pop(1)
    while num3[1][-1]==0 and len(num3[1])>1 :
        num3[1].pop(-1)
    
    
    num3[0].reverse()

    return num3

def division(a,b,decimales=101):
    a[0].reverse()
    b[0].reverse()
    if a[0][0]!=b[0][0]:
        signo=0
    else:
        signo=1
    signa=a[0][0]
    signb=b[0][0]
    del a[0][0]
    del b[0][0]
    c=[]
    d=[]
    divdecimal=""
    diventero=""
    for i in range (len(a[0])):
        c.append(a[0][i])
    for j in range (len(a[1])):
        c.append(a[1][j])
    if len(a[1])<len(b[1]):
        cero=len(b[1])-len(a[1])
        for k in range(cero):
            c.append(0)
    for l in range(len(b[0])):
        d.append(b[0][l])
    for m in range (len(b[1])):
        d.append(b[1][m])
    if len(b[1])<len(a[1]):
        cero=len(a[1])-len(b[1])
        for k in range(cero):
            d.append(0)
    num1=float("".join(str(n) for n in c))
    num2=float("".join(str(o) for o in d))
    diventero+=str(int(num1/num2))
    mod=(num1%num2)*10
    for p in range (decimales):
        rest=int(mod/num2)
        divdecimal+=str(rest)
        mod=(mod%num2)*10
    a0=list(map(int,diventero))
    a1=list(map(int,divdecimal))
    if signo==0:
        a0.insert(0,"-")
    if signo==1:
        a0.insert(0,"+")
    if decimales==101:
        if num1%num2==0:
            a1=[]
            a1.append(0)
        else:
            q=0
            while q==0:
                if a1[-1]=="0":
                    a1.pop(-1)
                else:
                    q=1
    resultado=(a0,a1)
    a[0].insert(0,signa)
    b[0].insert(0,signb)
    a[0].reverse()
    b[0].reverse()
    resultado[0].reverse()
    return(resultado)
            
def comparacion(a,b):
    if resta(a,b)==([0,'+'],[0]):
        print("las tuplas son iguales")
    else:
        print("las tuplas son diferentes")      

def pi(n):
    pi=0
    for k in range(n+1):
        pi += 2 * (-1)**k * 3**(1/2 - k) / (2 * k + 1)
    return pi


if __name__ == "__main__":
