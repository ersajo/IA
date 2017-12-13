from Escenario import *
from Archivo import *
from Character import *
from Arbol import *
import random
#-------------------------------------------------------------------------------
#def MoveAUTO
#def MoveMANUAL
#-------------------obteniendo mundo -------------------------------------------
texto = Archivo()
contenido = texto.read('labyrint0.txt')
BD_Char = Archivo()
costos = BD_Char.read('Characters.txt')
viewX = len(contenido[0])
viewY = len(contenido)-1
#-------------------------definiendo colores------------------------------------
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
#------------------------definiendo mundo visitado y real-----------------------

reloj = pygame.time.Clock()
view = Escenario(viewX, viewY)
view.paintWorld(contenido, 1)
view.copyWorld(viewX, viewY)
view.paintWorld(view.getSombra(), 0)
#------------------------colocando personaje/punto final------------------------
X = (random.randrange(viewX-1))*50
Y = (random.randrange(viewY-1))*50
PosChar = [X,Y]#Inicializacion del la posicion del monito
PosCharlast = [0,0]#posicion anterior del Character si efectua movimiento
FinalPoint=[(random.randrange(viewX-1)),(random.randrange(viewY-1))]#Posicion del Punto Final
monito = Character("Human",X,Y,costos)
dir=""

#-------------------------definiendo opciones de juego--------------------------
opc = 2#1 manual , 2 auntomatico -anchura-longitud-
#-------------------------------------------------------------------------------
def MoveAUTO():
    #------------------Menu-----------------------------------------------------
    pygame.init()
    Terminar = False
    print "elije tipo de busqueda"
    print "1.-Anchura"
    print "2.-Profundidad"
    #TSearch = raw_input("Chose One:")
    TSearch=1
    #---------------estableciendo cliterios de busqueda-------------------------
    priori=monito.askfor(1,2,3,4,view)
    print "orden de prioridad->"+str(priori)
    auxdir=0
    flag=True
    #-----------------------start Game------------------------------------------
    while not Terminar:

        #---Manejo de eventos
        for Evento in pygame.event.get():
           if Evento.type == pygame.QUIT:
                Terminar = True
#-----------------La logica del juego-------------------------------------------
        #------------cambiando direccion de character---------------------------
        #------PosChar reusado para registrar turno con o sin mov---------------
        if(PosChar[0]==monito.getX and PosChar[1]==monito.getY and flag==True and auxdir<=3):
            auxdir=auxdir+1
            dir=priori[auxdir]
        else:
            auxdir=0
            dir=priori[auxdir]
            flag=True

        #--------cambio de terreno al presionar con el mouse--------------------
        if(pygame.mouse.get_pressed()[2] != 0):
            view.changeTerrain()
            view.paintWorld(view.getWorld(), 1)
        #-----------salir del juego al presionar F3-----------------------------
        if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
            view.printArreglo()
            a=raw_input("ffdfgdf")
#-------------------------------------------------------------------------------
        #------registra posicion del character con o sin movimiento-------------
        PosChar[0]=monito.getX
        PosChar[1]=monito.getY
        #--------verifica acceso a direccion para desplazamiento----------------
        if(dir=="left"):
            print "left"
            if(view.askLEFT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.LEFT(view.askLEFT(monito.getX/50, monito.getY/50),1)

        if(dir=="right"):
            print "right"
            if(view.askRIGHT(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.RIGHT(view.askRIGHT(monito.getX/50, monito.getY/50),1)


        if(dir=="up"):
            print "up"
            if(view.askUP(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.UP(view.askUP(monito.getX/50, monito.getY/50),1)


        if(dir=="down"):
            print "down"
            if(view.askDOWN(monito.getX/50, monito.getY/50) != False):
                PosCharlast[0]=monito.getX/50
                PosCharlast[1]=monito.getY/50
                monito.DOWN(view.askDOWN(monito.getX/50, monito.getY/50),1)


    #------------definiendo nuevas caracteristicas de casilla visitada----------
        #----------comprueba la toma de desiciones------------------------------
        Decision = 0
        if(view.askUP(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askDOWN(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askRIGHT(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        if(view.askLEFT(monito.getX/50, monito.getY/50) > "0"):
            Decision = Decision + 1
        print Decision

        if(Decision >1):#--mas de 2 caminos disponibles es acreedor a desicion-
            d = "d"
        else:
            d = 0
        #re-define la casilla actual como no visitada
        view.getSombra()[PosCharlast[1]][PosCharlast[0]][4] = 0
        Visited = "v"
        Actual = "a"
        #el en turno cero se definen el punto inicial y final de lo contrario se fijan las caracteristicas de la casilla actual
        if(monito.getCostoT == 0):
            Inicio = "f"
            Shadow =view.getWorld()[FinalPoint[0]/50][FinalPoint[1]/50][0]#pintando casilla final
            view.getSombra()[FinalPoint[0]][FinalPoint[1]] = [Shadow,Inicio,0,0,0]#definiendo caracteristicas de a casilla final
            Inicio ="i"
        else:
            Inicio = 0

        Shadow =view.getSombra()[monito.getY/50][monito.getX/50][0]#pintando casila actual en mapa visitado
        view.getSombra()[monito.getY/50][monito.getX/50] = [Shadow,Inicio,Visited,d,Actual]#definiendo caracteristicas de la casilla actual

        #---------------------logica para Anchura-----------------------------------
        print "--->>>"+ str(view.getSombra()[monito.getY/50][monito.getX/50][3])
        if (TSearch==1):
            if(view.getSombra()[monito.getY/50][monito.getX/50][3]=="d"):
                print str(monito.Tree.elemento)+"->"+str(monito.getX/50)+","+str(monito.getY/50)+"->"+str(PosChar[0]/50)+","+str(PosChar[1]/50)
                monito.Tree.agregarElemento(monito.Tree,str(monito.getX/50)+","+str(monito.getY/50),str(PosChar[0])+","+str(PosChar[1]))
                print "soy"+str(monito.getX/50)+","+str(monito.getY/50)+"-mi papa es->"+str(PosChar[0])+","+str(PosChar[1])
                PosChar[0]=monito.getX/50
                PosChar[1]=monito.getY/50
                print monito.Tree.getFather(monito.Tree,str(monito.getX/50)+","+str(monito.getY/50))

        #-------------------logica para longitud------------------------------------
        if (TSearch==2):
            a=1
#-----------------------------------------------------------------------------
        view.paintWorld(view.getSombra(), 0)
        view.repaintCharacter(monito.getX, monito.getY, ROJO)

        if(pygame.mouse.get_pressed()[0] != 0):
            view.askTerrain()

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
    pygame.init()
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
        if(monito.getCostoT == 0):
            Inicio = "i"
        else:
            Inicio = 0

        view.getSombra()[PosCharlast[1]][PosCharlast[0]][4] = 0
        Actual = "a"
        Shadow =view.getSombra()[monito.getY/50][monito.getX/50][0]

        if(Decision > 2):
            d = "d"
        else:
            d = 0

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
