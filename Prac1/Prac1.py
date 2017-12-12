from Escenario import *
from Archivo import *
from Character import *
from Arbol import *
import random
#-----------------------------------------------------------------------------
#def MoveAUTO
#def MoveMANUAL
#------------------------------------------------------------------------------
texto = Archivo()
contenido = texto.read('labyrint0.txt')
BD_Char = Archivo()
costos = BD_Char.read('Characters.txt')
viewX = len(contenido[0])
viewY = len(contenido)-1
PosChar = [0,0]
PosCharlast = [0,0]
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
pygame.init()
reloj = pygame.time.Clock()
view = Escenario(viewX, viewY)
view.paintWorld(contenido, 1)
view.copyWorld(viewX, viewY)
view.paintWorld(view.getSombra(), 0)
X = (random.randrange(viewX-1))*50
Y = (random.randrange(viewY-1))*50
PosChar[0] = X
PosChar[1] = Y
monito = Character("Human",X,Y,costos)
FinalPoint=[(random.randrange(viewX-1)),(random.randrange(viewY-1))]
LastNode=[X,Y]
opc = 1


#------------------------------------------------------------------------------
def MoveAUTO():
    Terminar = False
    busca=Search()
    print "elije tipo de busqueda"
    print "1.-Anchura"
    print "2.-Profundidad"

    TSearch = raw_input("Chose One:")

    while not Terminar:
        #---Manejo de eventos
        for Evento in pygame.event.get():
           if Evento.type == pygame.QUIT:
                Terminar = True
        #---La logica del juego
        if(pygame.mouse.get_pressed()[2] != 0):
            view.changeTerrain()
            view.paintWorld(view.getWorld(), 1)

        if(pygame.key.get_pressed()[pygame.K_F3] != 0s):
            break
#------------------------------------------------------------------------------


        dir=monito.askfor(1,2,3,4)
        if(dir=="left"):

                if(view.askLEFT(monito.getX/50, monito.getY/50) != False):
                    PosCharlast[0]=monito.getX/50
                    PosCharlast[1]=monito.getY/50
                    monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50),1)

        if(dir=="right"):
            if(view.askRIGHT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50),1)

        if(dir=="up":)
            if(view.askUP(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.UP(view.askUP(monito.getX/50, monito.getY/50),1)

        if(dir=="down")
            if(view.askDOWN(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50),1)

    if (TSearch==1):


    if (TSearch==2):



#-----------------------------------------------------------------------------

        if(pygame.key.get_pressed()[pygame.K_UP] != 0):
            if(view.askUP(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.UP(view.askUP(monito.getX/50, monito.getY/50),1)

        if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
            if(view.askDOWN(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50),1)

        if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
            if(view.askRIGHT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50),1)

        if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
            if(view.askLEFT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50),1)

        view.paintWorld(view.getSombra(), 0)
        view.repaintCharacter(monito.getX, monito.getY, ROJO)

        if(pygame.mouse.get_pressed()[0] != 0):
            view.askTerrain()

        Decision = 0
        if(view.askUP(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askDOWN(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askRIGHT(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askLEFT(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1

        Visited = "v"
        view.getSombra()[PosCharlast[1]][PosCharlast[0]][4] = 0
        Actual = "a"


        if(Decision > 2):
            d = "d"
        else:
            d = 0

        if(monito.getCostoT == 0):
            Inicio = "f"
            Shadow =view.getWorld()[FinalPoint[0]][FinalPoint[1]][0]
            view.getSombra()[FinalPoint[0]][FinalPoint[1]] = [Shadow,Inicio,0,0,0]
            print "FP->"+str(FinalPoint[0]/50)+","+str(FinalPoint[1]/50)
            Inicio ="i"
        else:
            Inicio = 0

        Shadow =view.getSombra()[monito.getY/50][monito.getX/50][0]
        view.getSombra()[monito.getY/50][monito.getX/50] = [Shadow,Inicio,Visited,d,Actual]

        etiqueta = pygame.mouse.get_pos()
        string = "{0}"
        if (etiqueta[0] <= view.getDimensiones()[0] and etiqueta[1] <= view.getDimensiones()[1]):
            view.displayInfo(string.format(view.getSombra()[etiqueta[1]/50][etiqueta[0]/50]))

        #--Todos los dibujos van antes de esta linea
        pygame.display.flip()
        reloj.tick(10)  # Limitamos a 20 fotogramas por segundo
    pygame.quit()

#------------------------------------------------------------------------------
def MoveMANUAL():
    Terminar = False
    while not Terminar:
        #---Manejo de eventos
        for Evento in pygame.event.get():
           if Evento.type == pygame.QUIT:
                Terminar = True
        #---La logica del juego
        if(pygame.mouse.get_pressed()[2] != 0):
            view.changeTerrain()
            view.paintWorld(view.getWorld(), 1)

        if(pygame.key.get_pressed()[pygame.K_F3] != 0):
            break

        if(pygame.key.get_pressed()[pygame.K_UP] != 0):
            if(view.askUP(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.UP(view.askUP(monito.getX/50, monito.getY/50),1)

        if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
            if(view.askDOWN(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50),1)

        if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
            if(view.askRIGHT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50),1)

        if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
            if(view.askLEFT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50),1)

        view.paintWorld(view.getSombra(), 0)
        view.repaintCharacter(monito.getX, monito.getY, ROJO)

        if(pygame.mouse.get_pressed()[0] != 0):
            view.askTerrain()

        Decision = 0
        if(view.askUP(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askDOWN(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askRIGHT(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askLEFT(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1

        Visited = "v"
        view.getSombra()[PosCharlast[1]][PosCharlast[0]][4] = 0
        Actual = "a"


        if(Decision > 2):
            d = "d"
        else:
            d = 0

        if(monito.getCostoT == 0):
            Inicio = "f"
            Shadow =view.getWorld()[FinalPoint[0]][FinalPoint[1]][0]
            view.getSombra()[FinalPoint[0]][FinalPoint[1]] = [Shadow,Inicio,0,0,0]
            print "FP->"+str(FinalPoint[0]/50)+","+str(FinalPoint[1]/50)
            Inicio ="i"
        else:
            Inicio = 0

        Shadow =view.getSombra()[monito.getY/50][monito.getX/50][0]
        view.getSombra()[monito.getY/50][monito.getX/50] = [Shadow,Inicio,Visited,d,Actual]

        etiqueta = pygame.mouse.get_pos()
        string = "{0}"
        if (etiqueta[0] <= view.getDimensiones()[0] and etiqueta[1] <= view.getDimensiones()[1]):
            view.displayInfo(string.format(view.getSombra()[etiqueta[1]/50][etiqueta[0]/50]))

        #--Todos los dibujos van antes de esta linea
        pygame.display.flip()
        reloj.tick(10)  # Limitamos a 20 fotogramas por segundo
    pygame.quit()
# print "mi coordenada actual ->" +str(monito.getX/50)+","+str(monito.getY/50)+ " mi coordenada anterior ->" +str(PosCharlast[0])+","+str(PosCharlast[1])+"  Status-> "+str(view.getSombra()[monito.getX/50][monito.getY/50])

#------------------------------------------------------------------------------
print "Opciones"

if(opc == 1):
    MoveMANUAL()

if(opc == 2):
    MoveAUTO()
