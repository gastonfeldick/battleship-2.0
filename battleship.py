#from mimetypes import init

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
        self.image=pygame.image.load("puntero.png") 
        self.rect=self.image.get_rect()
        
                 
    
"""
def grilla():
    pass
    
    for x in range(20,350,33):
        for y in range(20,350,33):
            listaGrilla.append(pygame.draw.rect(screen,white,(x,y,32,32)))

    for x in range(400,700,33):
        for y in range(20,350,33):
            pygame.draw.rect(screen,white,(x,y,32,32)) """

# globales

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
#inicio

screen=pygame.display.set_mode((800,600))
backgroung=pygame.image.load("battleship-wallpapers.jpg").convert()

print(matriz)
i1=0
j1=0

for x in range(40,370,33):
    j1=0
    for y in range(40,370,33):
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
for x in range(420,720,33):
    j1=0
    for y in range(40,370,33):
        grilla=grid()
        grilla.rect.x=x
        grilla.rect.y=y
        grilla.tipo=mj2[i1][j1]
        listaGrilla2.add(grilla)
        j1+=1
    i1+=1
print(i1,j1)    
listaAuxiliarColisionados=pygame.sprite.Group()    
listaAuxiliarColisionadosJug2=pygame.sprite.Group()       
colision=pygame.sprite.Group()
cant=0 #cantidad de colisiones

colisionjug2=pygame.sprite.Group()

jugar=True
while jugar:
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
                    listaAuxiliarColisionados.add(pygame.sprite.spritecollide(raton,listaGrilla,True))
                    turno=2
                    print (listaAuxiliarColisionados)
            
        elif turno==2:        
        #colision jugador2
            colisionjug2=pygame.sprite.spritecollide(raton,listaGrilla2,False)
            for aux in colisionjug2:
                cant+=1
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cant>0 and cant<2:
                    listaAuxiliarColisionadosJug2.add(pygame.sprite.spritecollide(raton,listaGrilla2,True))
                    turno=1
                    print (listaAuxiliarColisionados)
            
    
    cant=0
    #fondo        
    screen.blit(backgroung,[0,0])
 
    #grilla
    listaGrilla.draw(screen)
    listaGrilla2.draw(screen)
    
    for coli in listaAuxiliarColisionados:
        if coli.tipo==1:
            coli.image.fill((0,0,0))
            print(coli.rect.x,coli.rect.y)
            #listaAuxiliarColisionados.remove(coli)
        elif coli.tipo==2:
            coli.image.fill((70,208,73))
        elif coli.tipo==3:
            coli.image.fill((183,183,183))
        elif coli.tipo==4:
            coli.image.fill((255,255,0))
        elif coli.tipo==0:
            coli.image.fill((0,0,255))
    listaAuxiliarColisionados.draw(screen)
    
    ganojug2[0]=0
    ganojug2[1]=0
    ganojug2[2]=0
    ganojug2[3]=0
    ganojug2[4]=0
    for coli in listaAuxiliarColisionadosJug2:
        if coli.tipo==1:
            coli.image.fill((0,0,0))
            print(coli.rect.x,coli.rect.y)
            ganojug2[0]+=1
            #listaAuxiliarColisionados.remove(coli)
        elif coli.tipo==2:
            coli.image.fill((70,208,73))
            ganojug2[1]+=1
        elif coli.tipo==3:
            coli.image.fill((183,183,183))
            ganojug2[2]+=1
        elif coli.tipo==4:
            coli.image.fill((255,255,0))
            ganojug2[3]+=1
        elif coli.tipo==0:
            coli.image.fill((0,0,255))
            ganojug2[4]+=1   
    listaAuxiliarColisionadosJug2.draw(screen)
    
    #ganador
    
    if gano[0]==4 and gano[1]==6 and gano[2]==6 and gano[3]==4:
        print("ganador jugador 2")
        jugar=False
        
    
    #mouse
    mouse_pos=pygame.mouse.get_pos()
    raton.rect.x=mouse_pos[0]
    raton.rect.y=mouse_pos[1]
    listaRaton.draw(screen)
    
    
    
    pygame.display.flip()
    
    #reloj.tick(60)