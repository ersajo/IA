from Escenario import *
from Archivo import *
from Character import *

texto = Archivo()
contenido = texto.read('labyrint0.txt')
BD_Char = Archivo()
costos = BD_Char.read('Characters.txt')
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
monito = Character("Human",0,0,costos)
while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
       if Evento.type == pygame.QUIT:
            Terminar = True
    #---La logica del juego
    if(pygame.mouse.get_pressed()[2] != 0):
        view.changeTerrain()
        view.paintWorld(contenido, 1)
    if(pygame.key.get_pressed()[pygame.K_F3] != 0):
        break
    if(pygame.key.get_pressed()[pygame.K_UP] != 0):
        if(monito.getY > 0 and view.askUP(monito.getX/50, monito.getY/50) <= '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.UP(view.askUP(monito.getX/50, monito.getY/50))
    if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
        if(monito.getY+50 < view.getDimensiones()[1] and view.askDOWN(monito.getX/50, monito.getY/50) < '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50))
    if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        if(monito.getX+50 < view.getDimensiones()[0] and view.askRIGHT(monito.getX/50, monito.getY/50) < '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50))
    if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        if(monito.getX > 0 and view.askLEFT(monito.getX/50, monito.getY/50) < '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50))
    #--Todos los dibujos van despues de esta linea
    view.paintWorld(view.getSombra(), 0)
    view.repaintCharacter(monito.getX, monito.getY, ROJO)
    if(pygame.mouse.get_pressed()[0] != 0):
        view.askTerrain()
    #--Todos los dibujos van antes de esta linea --
    pygame.display.flip()
    reloj.tick(10)  # Limitamos a 20 fotogramas por segundo
pygame.quit()
