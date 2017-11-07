from Escenario import *
from Archivo import *
from Character import *
import random

texto = Archivo()
contenido = texto.read('labyrint0.txt')
BD_Char = Archivo()
costos = BD_Char.read('Characters.txt')
viewY = len(contenido)-1
viewX = len(contenido[0])
PosChar = [0,0]
PosCharlast = [0,0]
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
pygame.init()
Terminar = False
reloj = pygame.time.Clock()
view = Escenario(viewX, viewY)
view.paintWorld(contenido, 1)
view.copyWorld(viewX, viewY)
view.paintWorld(view.getSombra(), 0)

PosChar[0] = (random.randrange(viewX-1))*50
PosChar[1] = (random.randrange(viewY-1))*50

monito = Character("Human",PosChar[0],PosChar[1],costos)

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
            PosCharlast[0]=monito.getX/50
            PosCharlast[1]=monito.getY/50
            monito.UP(view.askUP(monito.getX/50, monito.getY/50),1)

    if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
        if(monito.getY+50 < view.getDimensiones()[1] and view.askDOWN(monito.getX/50, monito.getY/50) < '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            PosCharlast[0]=monito.getX/50
            PosCharlast[1]=monito.getY/50
            monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50),1)

    if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        if(monito.getX+50 < view.getDimensiones()[0] and view.askRIGHT(monito.getX/50, monito.getY/50) < '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            PosCharlast[0]=monito.getX/50
            PosCharlast[1]=monito.getY/50
            monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50),1)

    if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        if(monito.getX > 0 and view.askLEFT(monito.getX/50, monito.getY/50) < '5'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            PosCharlast[0]=monito.getX/50
            PosCharlast[1]=monito.getY/50
            monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50),1)



    s =view.getSombra()[monito.getX/50][monito.getY/50][0]

    Desicion=0;
    if(monito.getY > 0 and monito.UP(view.askUP(monito.getX/50, monito.getY/50), 0) == 0):
        Desicion=Desicion+1
    if(monito.getY+50 < view.getDimensiones()[1] and monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50), 0) == 0):
        Desicion=Desicion+1
    if(monito.getX+50 < view.getDimensiones()[0] and monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50), 0) == 0):
        Desicion=Desicion+1
    if(monito.getX > 0 and monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50), 0) == 0):
        Desicion=Desicion+1

    v="v"
    if(monito.getCostoT == 0):
        i="i"
    else:
        i="0"

    view.getSombra()[PosCharlast[0]][PosCharlast[1]][3]=0
    a="a";

    if(Desicion>2):
        d="d"
    else:
        d="0"

    view.getSombra()[monito.getX/50][monito.getY/50] = [s,v,i,a,d]

    #--Todos los dibujos van despues de esta linea

    view.paintWorld(view.getSombra(), 0)
    view.repaintCharacter(monito.getX, monito.getY, ROJO)

<<<<<<< HEAD
    if(pygame.mouse.get_pressed()[0] != 0):
        view.askTerrain()

=======
>>>>>>> 577b1408ffb2e38ece8f220775044eefed1a52ea
    print "mi coordenada actual ->" +str(monito.getX/50)+","+str(monito.getY/50)+ " mi coordenada anterior ->" +str(PosCharlast[0])+","+str(PosCharlast[1])+"  Status-> "+str(view.getSombra()[monito.getX/50][monito.getY/50])
    #--Todos los dibujos van antes de esta linea
    pygame.display.flip()
    reloj.tick(10)  # Limitamos a 20 fotogramas por segundo
pygame.quit()
