import pygame, random
import time

class Escenario:

    Dimensiones = (750,900)
    Pantalla = pygame.display.set_mode(Dimensiones)
    World = []

    def __init__(self,viewX, viewY):
        self.Dimensiones = (viewX*50, viewY*50)
        Pantalla = pygame.display.set_mode(self.Dimensiones)
        pygame.draw.rect(Pantalla, (255, 0, 255), [0,0,50,50], 0)

    def repaintCharacter(self, X, Y, color):
        pygame.draw.rect(self.Pantalla, color, [X,Y,50,50], 0)

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
                    pygame.draw.rect(self.Pantalla, AZUL, [X,Y,50,50], 0)
                elif car == '1':
                    pygame.draw.rect(self.Pantalla, VERDE, [X,Y,50,50], 0)
                X = X + 50
            Y = Y + 50
            X = 0

    def askTerrain(self):
        p = pygame.mouse.get_pos()
        Num = self.World[p[1]/50][p[0]/50]
        myfont = pygame.font.SysFont("monospace bold", 30)
        if Num == '0':
            label = myfont.render("Azul", 1, (244,110,120))
            self.Pantalla.blit(label, (p[0], p[1]))
        elif Num == '1':
            label = myfont.render("Rosadito", 1, (244,110,120))
            self.Pantalla.blit(label, (p[0], p[1]))

    def askNow(self):
        p = pygame.mouse.get_pos()
        return self.World[p[1]/50][p[0]/50]

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

    tipo = ""
    distancia = 0
    costos = []
    costoT = 0
    X = 0
    Y = 0

    def __init__(self, tipo, X, Y, costos):
        self.tipo = tipo
        self.X = X
        self.Y = Y
        for i in range(len(costos)):
            if costos[i][0] == tipo:
                self.costos = costos[i]
                break
        print self.costos[1]

    def addCosto(self, mapa):
        print mapa
        self.costoT = self.costoT + self.costos[mapa + 1]
        print self.costoT

    @property
    def getX(self):
        return self.X

    @property
    def getY(self):
        return self.Y

    def UP(self):
        self.Y = self.Y-50

    def DOWN(self):
        self.Y = self.Y+50

    def RIGHT(self):
        self.X = self.X+50

    def LEFT(self):
        self.X = self.X-50


texto = Archivo()
contenido = texto.read('labyrint0.txt')
BD_Char = Archivo()
costos = BD_Char.read('Characters.txt')
viewY = len(contenido)-1
viewX = len(contenido[0])
NEGRO = (0, 0, 0)
ROJO = (254, 0, 0)
pygame.init()
Terminar = False
reloj = pygame.time.Clock()
view = Escenario(viewX, viewY)
view.paintWorld(contenido)
monito = Character("Sasquatch",0,0,costos)
while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
       if Evento.type == pygame.QUIT:
            Terminar = True
    #---La logica del juego
    if(pygame.key.get_pressed()[pygame.K_F12] != 0):
        view.paintWorld(contenido)
        view.askTerrain()
    if(pygame.key.get_pressed()[pygame.K_F3] != 0):
        break
    if(pygame.key.get_pressed()[pygame.K_UP] != 0):
        if(monito.getY > 0 and view.askUP(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.UP()
            monito.addCosto(view.askNow())
    if(pygame.key.get_pressed()[pygame.K_DOWN] != 0):
        if(monito.getY+50 < view.getDimensiones()[1] and view.askDOWN(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.DOWN()
            monito.addCosto(view.askNow())
    if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        if(monito.getX+50 < view.getDimensiones()[0] and view.askRIGHT(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(monito.getX, monito.getY,NEGRO)
            monito.RIGHT()
            monito.addCosto(view.askNow())
    if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        if(monito.getX > 0 and view.askLEFT(monito.getX/50, monito.getY/50) == '1'):
            view.repaintCharacter(mo0nito.getX, monito.getY,NEGRO)
            monito.LEFT()
            monito.addCosto(view.askNow())
    #--Todos los dibujos van despues de esta linea

    view.repaintCharacter(monito.getX, monito.getY, ROJO)
    #--Todos los dibujos van antes de esta linea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()
