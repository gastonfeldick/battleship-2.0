import os
import sys
from turtle import Screen

import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
reloj=pygame.time.Clock()
fondo=pygame.image.load("battleship-wallpapers.jpg")
ganador=pygame.image.load("winner.gif")

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    
    
    
    
    screen.blit(fondo,[0,0])
    
    screen.blit(ganador,[0,0])
    reloj.tick(20)
    pygame.display.flip()