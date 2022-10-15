import os
import sys
from turtle import Screen

import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
reloj=pygame.time.Clock()
fondo=pygame.image.load("battleship-wallpapers.jpg")

acorazado=pygame.image.load("imagenes/acorazado.png")
crucero=pygame.image.load("imagenes/crucero.png")
submarino=pygame.image.load("imagenes/submarn.png")
destructor=pygame.image.load("imagenes/destructor.png")

fuente=pygame.font.Font("Blood Squad.ttf",50)
texto=fuente.render("Player 1",0,(200,60,80))
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    
    
    
    
    screen.blit(fondo,[0,0])
    screen.blit(acorazado,[5,460])
    screen.blit(crucero,[270,500])
    screen.blit(submarino,[515,520])
    screen.blit(destructor,[650,540])
    screen.blit(texto,[10,10])
    
    reloj.tick(20)
    pygame.display.flip()