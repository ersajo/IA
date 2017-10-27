import pygame
from Archivo import *
from Escenario import *
from Character import *

texto = Archivo()
contenido = texto.read('labyrint0.txt')
viewY = len(contenido)-1
viewX = len(contenido[0])
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
pygame.init()
Terminar = False
reloj = pygame.time.Clock()
view = Escenario(viewX, viewY)
view.paintWorld(contenido, 1)
view.copyWorld(viewX, viewY)
view.paintWorld(view.getSombra(), 0)
monito = Character("Humano",0,0)
while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
       if Evento.type == pygame.QUIT:
            Terminar = True
    #---La logica del juego
    if(pygame.key.get_pressed()[pygame.K_UP] != 0):
        if(monito.getY > 0 and view.askUP(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.UP()
    if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
        if(monito.getY+50 < view.getDimensiones()[1] and view.askDOWN(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.DOWN()
    if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        if(monito.getX+50 < view.getDimensiones()[0] and view.askRIGHT(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.RIGHT()
    if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        if(monito.getX > 0 and view.askLEFT(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.LEFT()
    #--Todos los dibujos van despues de esta linea
    view.paintWorld(view.getSombra(), 0)
    view.repaintCharacter(monito.getX, monito.getY, ROJO)
    #--Todos los dibujos van antes de esta linea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()
