import pygame, random

class Escenario:

    Dimensiones = (375,450)
    Pantalla = pygame.display.set_mode(Dimensiones)
    World = []

    def __init__(self,viewX, viewY):
        self.Dimensiones = (viewX*25, viewY*25)
        Pantalla = pygame.display.set_mode(self.Dimensiones)
        pygame.draw.rect(Pantalla, (255, 0, 255), [0,0,25,25], 0)

    def repaintCharacter(self, X, Y, color):
        pygame.draw.rect(self.Pantalla, color, [X,Y,25,25], 0)

    def getDimensiones(self):
        return self.Dimensiones

    def paintWorld(self, contenido):
        self.World = contenido
        VERDE = (0, 255, 0)
        AZUL = (0, 0, 255)
        X = 0
        Y = 0
        for line in contenido:
            for car in line:
                if car == '0':
                    pygame.draw.rect(self.Pantalla, AZUL, [X,Y,25,25], 0)
                elif car == '1':
                    pygame.draw.rect(self.Pantalla, VERDE, [X,Y,25,25], 0)
                X = X + 25
            Y = Y + 25
            X = 0

    def askUP(self,charX,charY):
        return self.World[charY-1][charX]

    def askDOWN(self,charX,charY):
        return self.World[charY+1][charX]

    def askLEFT(self,charX,charY):
        return self.World[charY][charX-1]

    def askRIGHT(self,charX,charY):
        return self.World[charY][charX+1]

class Archivo:

    def read(self, ruta):
        with open(ruta, 'r') as leer:
            contenido = leer.read().split('\n')
        i = 0
        for line in contenido:
            contenido[i] = line.split(',')
            i = i + 1
        return contenido

class Character:

    tipo = "Monito"
    distancia = 0
    costo = 0
    X = 0
    Y = 0

    def __init__(self, tipo, X, Y):
        self.tipo = tipo
        self.X = X
        self.Y = Y

    @property
    def getX(self):
        return self.X

    @property
    def getY(self):
        return self.Y

    def UP(self):
        self.Y = self.Y-25

    def DOWN(self):
        self.Y = self.Y+25

    def RIGHT(self):
        self.X = self.X+25

    def LEFT(self):
        self.X = self.X-25


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
view.paintWorld(contenido)
monito = Character("Humano",0,0)
while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
       if Evento.type == pygame.QUIT:
            Terminar = True
    #---La logica del juego
    if(pygame.key.get_pressed()[pygame.K_F3] != 0):
        break
    if(pygame.key.get_pressed()[pygame.K_UP] != 0):
        if(monito.getY > 0 and view.askUP(monito.getX/25, monito.getY/25) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.UP()
    if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
        if(monito.getY+25 < view.getDimensiones()[1] and view.askDOWN(monito.getX/25, monito.getY/25) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.DOWN()
    if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        if(monito.getX+25 < view.getDimensiones()[0] and view.askRIGHT(monito.getX/25, monito.getY/25) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.RIGHT()
    if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        if(monito.getX > 0 and view.askLEFT(monito.getX/25, monito.getY/25) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.LEFT()
    #--Todos los dibujos van despues de esta linea

    view.repaintCharacter(monito.getX, monito.getY, ROJO)
    #--Todos los dibujos van antes de esta linea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()
