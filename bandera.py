import sys

import pygame

pygame.init()

class puntero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("imagenes/puntero.png") 
        self.rect=self.image.get_rect()

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
        
        
listaRaton=pygame.sprite.Group()
listaGanadora=pygame.sprite.Group()       
pygame.mouse.set_visible(0)
raton=puntero()
listaRaton.add(raton)    

  
  
listaBandera=pygame.sprite.Group()  
listaBanderaSeleccionada=pygame.sprite.Group()
listaBotones=pygame.sprite.Group()  

seleccionjugador=1

cargarBanderas()
fuente=pygame.font.Font("fuente/Blood Squad.ttf",40)
textop1=fuente.render("Player 1",0,(249,0,0))
textop2=fuente.render("Player 2",0,(249,0,0))
winner=pygame.image.load("imagenes/ganador1.png")

screen=pygame.display.set_mode((800,600))
backgroung=pygame.image.load("imagenes/battleship-wallpapers.jpg").convert()
menu=0
gano=2
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
                colision=pygame.sprite.spritecollide(raton,listaBotones,False)
                if colision:
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

    else: 
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    
        screen.fill((0,0,0))
        aux=0
        for gan in listaBanderaSeleccionada:   
            if gano==1 and aux==0:
                gan.rect.x=300
                gan.rect.y=70
                listaGanadora.add(gan)
            elif gano==2 and aux==1:
                gan.rect.x=300
                gan.rect.y=70
                listaGanadora.add(gan)
            aux+=1
        listaGanadora.draw(screen)
        screen.blit(winner,[200,200])
        pygame.display.flip()
           
        