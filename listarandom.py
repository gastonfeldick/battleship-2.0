import random
import time

def rinicio2():
    
    for i in range(0,10):
        #print(i)
        for j in range(0,10):
            matriz[i][j]=0
            mj2[i][j]=0
    
        
    #print(matriz)
    #print(mj2)
        
    #print("tiempo")
    time.sleep(0.5)
    #print("reinicio\n")
    #print (matriz)
    #print (mj2)
    
    #submarinos
    i=0
    while i<4:
        f=random.randint(0,9)
        c=random.randint(0,8)
        if  matriz[f][c]!=0:
            #print("repetido submarino")
            pass

        else:
            matriz[f][c]=1
            i+=1

    #destructores
    hv=random.randint(0,1)
    i=0
    while i<3:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,7)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 :
                #print("repetido destructor")
                pass
            else:
                matriz[f][c]=2
                matriz[f][c+1]=2
                i+=1
        else:#vertical
            f=random.randint(0,8)
            c=random.randint(0,8)
            if  matriz[f+1][c]!=0 or matriz[f][c]!=0 :
                #print("repetido destructor")
                pass
            else:
                matriz[f][c]=2
                matriz[f+1][c]=2
                i+=1
        hv=random.randint(0,1)

    #cruceros

    hv=random.randint(0,1)
    i=0
    while i<2:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,6)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0:
                    #print("repetido cruceros")
                    pass
            else:
                matriz[f][c]=3
                matriz[f][c+1]=3
                matriz[f][c+2]=3
                i+=1
        else:
            f=random.randint(0,7)
            c=random.randint(0,8)
            if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 :
                #print("repetido cruceros")
                pass
            else:
                matriz[f][c]=3
                matriz[f+1][c]=3
                matriz[f+2][c]=3
                i+=1
        hv=random.randint(0,1)
        
    #acorazado
    hv=random.randint(0,1)
    i=0
    if hv==0:#horizontal
        while i==0:
            f=random.randint(0,9)
            c=random.randint(0,5)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0 or matriz[f][c+3]!=0:
                #print("repetido acorazado")
                pass
            else:
                matriz[f][c]=4
                matriz[f][c+1]=4
                matriz[f][c+2]=4
                matriz[f][c+3]=4
                i=1
    else:
        while i==0:
            
            f=random.randint(0,6)
            c=random.randint(0,8)
            if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 or matriz[f+3][c]!=0 :
                #print("repetido acorazado")
                pass
            else:
                matriz[f][c]=4
                matriz[f+1][c]=4
                matriz[f+2][c]=4
                matriz[f+3][c]=4
                i+=1
                
                
    #print(matriz)


    #jugador 2
        #submarinos2
    i=0
    while i<4:
        f=random.randint(0,9)
        c=random.randint(0,8)
        if  mj2[f][c]!=0:
            #print("repetido")
            pass

        else:
            mj2[f][c]=1
            i+=1
            
    #destructores2

    hv=random.randint(0,1)
    i=0
    while i<3:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,7)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 :
                #print("repetido destructor")
                pass
            else:
                mj2[f][c]=2
                mj2[f][c+1]=2
                i+=1
        else:#vertical
            f=random.randint(0,8)
            c=random.randint(0,8)
            if  mj2[f+1][c]!=0 or mj2[f][c]!=0 :
                #print("repetido destructor")
                pass
            else:
                mj2[f][c]=2
                mj2[f+1][c]=2
                i+=1
        hv=random.randint(0,1)

    #cruceros2
        
    hv=random.randint(0,1)
    i=0
    while i<2:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,6)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0:
                #print("repetido cruceros")
                pass
            else:
                mj2[f][c]=3
                mj2[f][c+1]=3
                mj2[f][c+2]=3
                i+=1
        else:
            f=random.randint(0,7)
            c=random.randint(0,8)
            if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 :
                #print("repetido cruceros")
                pass
            else:
                mj2[f][c]=3
                mj2[f+1][c]=3
                mj2[f+2][c]=3
                i+=1
        hv=random.randint(0,1)
            
    #acorazado2
    hv=random.randint(0,1)
    i=0
    if hv==0:#horizontal
        while i==0:
            f=random.randint(0,9)
            c=random.randint(0,5)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0 or mj2[f][c+3]!=0:
                #print("repetido destructor")
                pass
            else:
                mj2[f][c]=4
                mj2[f][c+1]=4
                mj2[f][c+2]=4
                mj2[f][c+3]=4
                i=1
    else:
        while i==0:
            
            f=random.randint(0,6)
            c=random.randint(0,8)
            if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 or mj2[f+3][c]!=0 :
                #print("repetido destructor")
                pass
            else:
                mj2[f][c]=4
                mj2[f+1][c]=4
                mj2[f+2][c]=4
                mj2[f+3][c]=4
                i+=1



"""
i=0
j=0
lista=[]
aux=[]
while i<10:
    while j<10:
        list. 
        j+=1
    i+=1
"""
matriz = [[0 for i in range(10)] for i in range(10)] # matriz jugador1
mj2 =  [[0 for i in range(10)] for i in range(10)] # matriz jugador2


for m in matriz:
    m=0
#print (matriz)
 #submarinos
i=0
while i<4:
    f=random.randint(0,9)
    c=random.randint(0,8)
    if  matriz[f][c]!=0:
        #print("repetido submarino")
        pass
    else:
        matriz[f][c]=1
        i+=1

#destructores
hv=random.randint(0,1)
i=0
while i<3:
    if hv==0:#horizontal
        f=random.randint(0,9)
        c=random.randint(0,7)
        if  matriz[f][c]!=0 or matriz[f][c+1]!=0 :
            #print("repetido destructor")
            pass
        else:
            matriz[f][c]=2
            matriz[f][c+1]=2
            i+=1
    else:#vertical
        f=random.randint(0,8)
        c=random.randint(0,8)
        if  matriz[f+1][c]!=0 or matriz[f][c]!=0 :
            #print("repetido destructor")
            pass
        else:
            matriz[f][c]=2
            matriz[f+1][c]=2
            i+=1
    hv=random.randint(0,1)

#cruceros

hv=random.randint(0,1)
i=0
while i<2:
    if hv==0:#horizontal
        f=random.randint(0,9)
        c=random.randint(0,6)
        if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0:
                #print("repetido cruceros")
                pass
        else:
            matriz[f][c]=3
            matriz[f][c+1]=3
            matriz[f][c+2]=3
            i+=1
    else:
        f=random.randint(0,7)
        c=random.randint(0,8)
        if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 :
            #print("repetido cruceros")
            pass
        else:
            matriz[f][c]=3
            matriz[f+1][c]=3
            matriz[f+2][c]=3
            i+=1
    hv=random.randint(0,1)
    
#acorazado
hv=random.randint(0,1)
i=0
if hv==0:#horizontal
    while i==0:
        f=random.randint(0,9)
        c=random.randint(0,5)
        if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0 or matriz[f][c+3]!=0:
            #print("repetido acorazado")
            pass
        else:
            matriz[f][c]=4
            matriz[f][c+1]=4
            matriz[f][c+2]=4
            matriz[f][c+3]=4
            i=1
else:
    while i==0:
        
        f=random.randint(0,6)
        c=random.randint(0,8)
        if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 or matriz[f+3][c]!=0 :
            #print("repetido acorazado")
            pass
        else:
            matriz[f][c]=4
            matriz[f+1][c]=4
            matriz[f+2][c]=4
            matriz[f+3][c]=4
            i+=1
            
            
#print(matriz)


#jugador 2
    #submarinos2
i=0
while i<4:
    f=random.randint(0,9)
    c=random.randint(0,8)
    if  mj2[f][c]!=0:
        print("repetido")

    else:
        mj2[f][c]=1
        i+=1
           
#destructores2

hv=random.randint(0,1)
i=0
while i<3:
    if hv==0:#horizontal
        f=random.randint(0,9)
        c=random.randint(0,7)
        if  mj2[f][c]!=0 or mj2[f][c+1]!=0 :
            #print("repetido destructor")
            pass
        else:
            mj2[f][c]=2
            mj2[f][c+1]=2
            i+=1
    else:#vertical
        f=random.randint(0,8)
        c=random.randint(0,8)
        if  mj2[f+1][c]!=0 or mj2[f][c]!=0 :
            #print("repetido destructor")
            pass
        else:
            mj2[f][c]=2
            mj2[f+1][c]=2
            i+=1
    hv=random.randint(0,1)

#cruceros2
    
hv=random.randint(0,1)
i=0
while i<2:
    if hv==0:#horizontal
        f=random.randint(0,9)
        c=random.randint(0,6)
        if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0:
            #print("repetido cruceros")
            pass
        else:
            mj2[f][c]=3
            mj2[f][c+1]=3
            mj2[f][c+2]=3
            i+=1
    else:
        f=random.randint(0,7)
        c=random.randint(0,8)
        if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 :
            #print("repetido cruceros")
            pass
        else:
            mj2[f][c]=3
            mj2[f+1][c]=3
            mj2[f+2][c]=3
            i+=1
    hv=random.randint(0,1)
        
#acorazado2
hv=random.randint(0,1)
i=0
if hv==0:#horizontal
    while i==0:
        f=random.randint(0,9)
        c=random.randint(0,5)
        if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0 or mj2[f][c+3]!=0:
            #print("repetido destructor")
            pass
        else:
            mj2[f][c]=4
            mj2[f][c+1]=4
            mj2[f][c+2]=4
            mj2[f][c+3]=4
            i=1
else:
    while i==0:
        
        f=random.randint(0,6)
        c=random.randint(0,8)
        if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 or mj2[f+3][c]!=0 :
            #print("repetido destructor")
            pass
        else:
            mj2[f][c]=4
            mj2[f+1][c]=4
            mj2[f+2][c]=4
            mj2[f+3][c]=4
            i+=1


####################################
####################################
####################################


def reiniciarMatriz():
    for m in matriz:
        m=0
    for n in mj2:
        n=0
    
    print(matriz)
    print(mj2)
    
    
    print("estoy ")

    #submarinos
    i=0
    while i<4:
        f=random.randint(0,9)
        c=random.randint(0,8)
        if  matriz[f][c]!=0:
            print("repetido submarino")

        else:
            matriz[f][c]=1
            i+=1

    #destructores
    hv=random.randint(0,1)
    i=0
    while i<3:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,7)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 :
                print("repetido destructor")
            else:
                matriz[f][c]=2
                matriz[f][c+1]=2
                i+=1
        else:#vertical
            f=random.randint(0,8)
            c=random.randint(0,8)
            if  matriz[f+1][c]!=0 or matriz[f][c]!=0 :
                print("repetido destructor")
            else:
                matriz[f][c]=2
                matriz[f+1][c]=2
                i+=1
        hv=random.randint(0,1)

    #cruceros

    hv=random.randint(0,1)
    i=0
    while i<2:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,6)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0:
                    print("repetido cruceros")
            else:
                matriz[f][c]=3
                matriz[f][c+1]=3
                matriz[f][c+2]=3
                i+=1
        else:
            f=random.randint(0,7)
            c=random.randint(0,8)
            if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 :
                print("repetido cruceros")
            else:
                matriz[f][c]=3
                matriz[f+1][c]=3
                matriz[f+2][c]=3
                i+=1
        hv=random.randint(0,1)
        
    #acorazado
    hv=random.randint(0,1)
    i=0
    if hv==0:#horizontal
        while i==0:
            f=random.randint(0,9)
            c=random.randint(0,5)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0 or matriz[f][c+3]!=0:
                print("repetido acorazado")
            else:
                matriz[f][c]=4
                matriz[f][c+1]=4
                matriz[f][c+2]=4
                matriz[f][c+3]=4
                i=1
    else:
        while i==0:
            
            f=random.randint(0,6)
            c=random.randint(0,8)
            if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 or matriz[f+3][c]!=0 :
                print("repetido acorazado")
            else:
                matriz[f][c]=4
                matriz[f+1][c]=4
                matriz[f+2][c]=4
                matriz[f+3][c]=4
                i+=1
                
                
    #print(matriz)


    #jugador 2
        #submarinos2
    i=0
    while i<4:
        f=random.randint(0,9)
        c=random.randint(0,8)
        if  mj2[f][c]!=0:
            print("repetido")

        else:
            mj2[f][c]=1
            i+=1
            
    #destructores2

    hv=random.randint(0,1)
    i=0
    while i<3:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,7)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 :
                print("repetido destructor")
            else:
                mj2[f][c]=2
                mj2[f][c+1]=2
                i+=1
        else:#vertical
            f=random.randint(0,8)
            c=random.randint(0,8)
            if  mj2[f+1][c]!=0 or mj2[f][c]!=0 :
                print("repetido destructor")
            else:
                mj2[f][c]=2
                mj2[f+1][c]=2
                i+=1
        hv=random.randint(0,1)

    #cruceros2
        
    hv=random.randint(0,1)
    i=0
    while i<2:
        if hv==0:#horizontal
            f=random.randint(0,9)
            c=random.randint(0,6)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0:
                print("repetido cruceros")
            else:
                mj2[f][c]=3
                mj2[f][c+1]=3
                mj2[f][c+2]=3
                i+=1
        else:
            f=random.randint(0,7)
            c=random.randint(0,8)
            if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 :
                print("repetido cruceros")
            else:
                mj2[f][c]=3
                mj2[f+1][c]=3
                mj2[f+2][c]=3
                i+=1
        hv=random.randint(0,1)
            
    #acorazado2
    hv=random.randint(0,1)
    i=0
    if hv==0:#horizontal
        while i==0:
            f=random.randint(0,9)
            c=random.randint(0,5)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0 or mj2[f][c+3]!=0:
                print("repetido destructor")
            else:
                mj2[f][c]=4
                mj2[f][c+1]=4
                mj2[f][c+2]=4
                mj2[f][c+3]=4
                i=1
    else:
        while i==0:
            
            f=random.randint(0,6)
            c=random.randint(0,8)
            if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 or mj2[f+3][c]!=0 :
                print("repetido destructor")
            else:
                mj2[f][c]=4
                mj2[f+1][c]=4
                mj2[f+2][c]=4
                mj2[f+3][c]=4
                i+=1
    print(matriz)
    print(mj2)





#print("inicio")
#print(matriz)
#print(mj2)


    


#print("reinci")
#print(matriz)
#print(mj2)

