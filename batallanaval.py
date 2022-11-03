import sys
from os import system
from pickle import FALSE

import pygame

from listarandom import *

pygame.init()

class grid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((32,32))
        self.color="white"
        self.tipo=0
        self.image.fill(white)
        self.rect=self.image.get_rect()

class puntero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("imagenes/puntero.png") 
        self.rect=self.image.get_rect()
        
def cargar():
        
    print(matriz)
    i1=0
    j1=0

    for x in range(40,370,33):
        j1=0
        for y in range(20,350,33):
            grilla=grid()
            grilla.rect.x=x
            grilla.rect.y=y
            grilla.tipo=matriz[i1][j1]
            listaGrilla.add(grilla)
            j1+=1
        i1+=1
    print(i1,j1)

    i1=0
    j1=0
    for x in range(430,730,33):
        j1=0
        for y in range(20,350,33):
            grilla=grid()
            grilla.rect.x=x
            grilla.rect.y=y
            grilla.tipo=mj2[i1][j1]
            listaGrilla2.add(grilla)
            j1+=1
        i1+=1            


class bandera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("banderas/rusia.jpeg")
        self.rect=self.image.get_rect()
        self.jugador=0
    def update(self):
            self.kill()

class botones(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("banderas/play.png")
        self.rect=self.image.get_rect()
    def update(self):
            self.kill()

def cargarBanderas():
    
    i=0
    while i<=5:
        objetoBandera=bandera()
        if(i==0):
            objetoBandera.image= pygame.image.load("banderas/argentina.png")
            objetoBandera.rect.x=70
            objetoBandera.rect.y=100
        elif(i==1):
            objetoBandera.image= pygame.image.load("banderas/brasil.jpg")
            objetoBandera.rect.x=300
            objetoBandera.rect.y=100
        elif(i==2):
            objetoBandera.image= pygame.image.load("banderas/canada.png")
            objetoBandera.rect.x=530
            objetoBandera.rect.y=100
        elif(i==3):
            objetoBandera.image= pygame.image.load("banderas/china.png")
            objetoBandera.rect.x=70
            objetoBandera.rect.y=250
        elif(i==4):
            objetoBandera.image= pygame.image.load("banderas/eeuu.jpeg")
            objetoBandera.rect.x=300
            objetoBandera.rect.y=250
        elif(i==5):
            objetoBandera.image= pygame.image.load("banderas/rusia.jpeg")
            objetoBandera.rect.x=530
            objetoBandera.rect.y=250
        listaBandera.add(objetoBandera)   
        i+=1
    
def cargarBotones():
    i=0
    while i<=1:
        btn=botones()
        if i==0:
            btn.image=pygame.image.load("banderas/play.png")
            btn.rect.x=300
            btn.rect.y=300
            listaBotones.add(btn)
        elif i==1:
            btn.image=pygame.image.load("banderas/reset.png")
            btn.rect.x=420
            btn.rect.y=327
            listaBotones.add(btn)
        i+=1
        
white=(255,255,255)
listaGrilla=pygame.sprite.Group()
listaGrilla2=pygame.sprite.Group()
listaRaton=pygame.sprite.Group()
reloj=pygame.time.Clock()
pygame.mouse.set_visible(0)
raton=puntero()
listaRaton.add(raton)
turno=1
ganojug1=[0,0,0,0,0]
ganojug2=[0,0,0,0,0]

acorazado=pygame.image.load("imagenes/acorazado.png")
crucero=pygame.image.load("imagenes/crucero.png")
submarino=pygame.image.load("imagenes/submarn.png")
destructor=pygame.image.load("imagenes/destructor.png")
mano=pygame.image.load("imagenes/mano.png")


  
  
listaBandera=pygame.sprite.Group()  
listaBanderaSeleccionada=pygame.sprite.Group()
listaBotones=pygame.sprite.Group()  

seleccionjugador=1

cargarBanderas()
fuente=pygame.font.Font("fuente/Blood Squad.ttf",40)
textop1=fuente.render("Player 1",0,(249,0,0))
textop2=fuente.render("Player 2",0,(249,0,0))

cargar()

listaAuxiliarColisionados=pygame.sprite.Group()    
listaAuxiliarColisionadosJug2=pygame.sprite.Group()       
colision=pygame.sprite.Group()
cant=0 #cantidad de colisiones

colisionjug2=pygame.sprite.Group()

jugar=True
gano=0
listaGanadora=pygame.sprite.Group()

screen=pygame.display.set_mode((800,600))
backgroung=pygame.image.load("imagenes/battleship-wallpapers.jpg").convert()
winner=pygame.image.load("imagenes/ganador1.png")
menu=0

sonido1=pygame.mixer.Sound("bomba.wav")


while True:
    
    if menu==0:
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
            if(seleccionjugador==1 or seleccionjugador==2):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    listaBanderaSeleccionada.add(pygame.sprite.spritecollide(raton,listaBandera,True))
                    cont=0
                    for banderita in listaBanderaSeleccionada:
                        if cont==0:
                            banderita.rect.x=100
                            banderita.rect.y=400
                            banderita.jugador=1
                            seleccionjugador=2
                        elif cont==1:
                            banderita.rect.x=500
                            banderita.rect.y=400
                            banderita.jugador=2
                            seleccionjugador=3
                        elif cont>=2:
                            banderita.update()
                        cont+=1
                    
            
            if seleccionjugador>2:     
                for banderita in listaBandera:
                    banderita.update()
                cargarBotones()
            if event.type==pygame.MOUSEBUTTONDOWN:
                colisionMenu=pygame.sprite.spritecollide(raton,listaBotones,False)
                if colisionMenu:
                    menu=1
                
        screen.fill((0,0,0))
        
        screen.blit(textop1,[145,550])
        screen.blit(textop2,[540,550])
        
        listaBandera.draw(screen)
        listaBotones.draw(screen)
        listaBanderaSeleccionada.draw(screen)
        
        mouse_pos=pygame.mouse.get_pos()
        raton.rect.x=mouse_pos[0]
        raton.rect.y=mouse_pos[1]
        listaRaton.draw(screen)
        
        
        pygame.display.flip()

    elif menu==1:
        colision=()
        colisionjug2=()
        pygame.sprite.Group.remove(listaAuxiliarColisionados)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                
            #colision jugador1
            if(turno==1):
                colision=pygame.sprite.spritecollide(raton,listaGrilla,False)
                for aux in colision:
                    cant+=1
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if cant>0 and cant<2:
                        agrega=pygame.sprite.spritecollide(raton,listaGrilla,False)
                        if agrega:
                            for en in agrega:
                                if en.tipo==1 or en.tipo==2 or en.tipo==3 or en.tipo==4:
                                    sonido1.play()
                                    sonido1.set_volume(1.0)

                        listaAuxiliarColisionados.add(pygame.sprite.spritecollide(raton,listaGrilla,True))
                        turno=2
                        #print (listaAuxiliarColisionados)
                
            elif turno==2:        
            #colision jugador2s
                colisionjug2=pygame.sprite.spritecollide(raton,listaGrilla2,False)
                for aux in colisionjug2:
                    cant+=1
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if cant>0 and cant<2:
                        agrega2=pygame.sprite.spritecollide(raton,listaGrilla2,False)
                        if agrega2:
                            for en in agrega2:
                                if en.tipo==1 or en.tipo==2 or en.tipo==3 or en.tipo==4:
                                    sonido1.play()
                                    sonido1.set_volume(1.0)


                        listaAuxiliarColisionadosJug2.add(pygame.sprite.spritecollide(raton,listaGrilla2,True))
                        
                        turno=1
                        #print (listaAuxiliarColisionados)
                
        
        cant=0
        #fondo        
        screen.blit(backgroung,[0,0])
    
        #grilla
        listaGrilla.draw(screen)
        listaGrilla2.draw(screen)
        ganojug1[0]=0
        ganojug1[1]=0
        ganojug1[2]=0
        ganojug1[3]=0
        ganojug1[4]=0
        for coli in listaAuxiliarColisionados:
            if coli.tipo==1:
                coli.image.fill((0,255,64))
                #print(coli.rect.x,coli.rect.y)
                ganojug1[0]+=1
                #listaAuxiliarColisionados.remove(coli)
            elif coli.tipo==2:
                coli.image.fill((255,255,0))
                ganojug1[1]+=1
            elif coli.tipo==3:
                coli.image.fill((255,0,0))
                ganojug1[2]+=1
            elif coli.tipo==4:
                coli.image.fill((192,192,192))
                ganojug1[3]+=1
            elif coli.tipo==0:
                coli.image.fill((0,0,255))
                ganojug1[4]+=1
        listaAuxiliarColisionados.draw(screen)
        
        ganojug2[0]=0
        ganojug2[1]=0
        ganojug2[2]=0
        ganojug2[3]=0
        ganojug2[4]=0
        
        for coli in listaAuxiliarColisionadosJug2:
            if coli.tipo==1:
                coli.image.fill((0,255,64))
                #print(coli.rect.x,coli.rect.y)
                ganojug2[0]+=1
                #listaAuxiliarColisionados.remove(coli)
            elif coli.tipo==2:
                coli.image.fill((255,255,0))
                ganojug2[1]+=1
            elif coli.tipo==3:
                coli.image.fill((255,0,0))
                ganojug2[2]+=1
            elif coli.tipo==4:
                coli.image.fill((192,192,192))
                ganojug2[3]+=1
            elif coli.tipo==0:
                coli.image.fill((0,0,255))
                ganojug2[4]+=1   
        listaAuxiliarColisionadosJug2.draw(screen)
        
        
        screen.blit(acorazado,[5,460])
        screen.blit(crucero,[270,500])
        screen.blit(submarino,[515,520])
        screen.blit(destructor,[650,540])
        z=0
        for l in listaBanderaSeleccionada:
            if z==0:
                l.rect=(40,380)
            if z==1:
                l.rect=(430,380)
            z+=1
        listaBanderaSeleccionada.draw(screen)
        #screen.blit(textop1,[145,0])
        #screen.blit(textop2,[540,0])
        
        #mano ganador
        
        if turno==1:
            screen.blit(mano,[260,400])
        elif turno==2:
            screen.blit(mano,[650,400])
        #ganador
        
        if ganojug1[0]==4 and ganojug1[1]==6 and ganojug1[2]==6 and ganojug1[3]==4:
            print("ganador jugador 1")
            gano=1
            menu=2
            jugar=False
        elif ganojug2[0]==4 and ganojug2[1]==6 and ganojug2[2]==6 and ganojug2[3]==4:
            print("ganador jugador 2")
            gano=2
            menu=2
            jugar=False    
        
        #mouse
        mouse_pos=pygame.mouse.get_pos()
        raton.rect.x=mouse_pos[0]
        raton.rect.y=mouse_pos[1]
        listaRaton.draw(screen)

        pygame.display.flip()
        
    elif menu==2:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    
        screen.fill((0,0,0))
        este=0
        for gan in listaBanderaSeleccionada:   
            if gano==1 and este==0:
                gan.rect=(300,70)
                listaGanadora.add(gan)
            elif gano==2 and este==1:
                gan.rect=(300,70)
                listaGanadora.add(gan)
            este+=1
        listaGanadora.draw(screen)
        screen.blit(winner,[200,200])
        pygame.display.flip()
           
        
        

    reloj.tick(60)
            