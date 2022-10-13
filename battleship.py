#from mimetypes import init
import random
import sys
from os import system
from pickle import FALSE
from listarandom import *
import pygame

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

#inicio

screen=pygame.display.set_mode((800,600))
backgroung=pygame.image.load("battleship-wallpapers.jpg").convert()

print(matriz)
i1=0
j1=0

for x in range(20,350,33):
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

for x in range(400,700,33):
        for y in range(20,350,33):
            grilla=grid()
            grilla.rect.x=x
            grilla.rect.y=y
            listaGrilla2.add(grilla)     
listaAuxiliarColisionados=pygame.sprite.Group()           
colision=pygame.sprite.Group()
cant=0 #cantidad de colisiones
while True:
    colision=()
    pygame.sprite.Group.remove(listaAuxiliarColisionados)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        colision=pygame.sprite.spritecollide(raton,listaGrilla,False)
        for aux in colision:
            cant+=1
        if event.type==pygame.MOUSEBUTTONDOWN:
            if cant>0 and cant<2:
                listaAuxiliarColisionados.add(pygame.sprite.spritecollide(raton,listaGrilla,True))
                
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
    #mouse
    mouse_pos=pygame.mouse.get_pos()
    raton.rect.x=mouse_pos[0]
    raton.rect.y=mouse_pos[1]
    listaRaton.draw(screen)
    
    listaAuxiliarColisionados.draw(screen)
    
    pygame.display.flip()
    
    #reloj.tick(60)