from Arbol import *
class Character:

    tipo = ""
    distancia = 0
    costos = []
    costoT = 0
    X = 0
    Y = 0
    Tree=Arbol("0,0")

    def __init__(self, tipo, X, Y, costos):
        self.tipo = tipo
        self.X = X
        self.Y = Y
        Tree=Arbol(str(self.X)+","+str(self.Y))
        for i in range(len(costos)):
            if costos[i][0] == tipo:
                self.costos = costos[i]
                break

    @property
    def getX(self):
        return self.X

    @property
    def getY(self):
        return self.Y

    @property
    def getCostoT(self):
        return self.costoT

    @property
    def getcostos(self):
        return self.costos

    def askMove(self, mapa):
        return self.costos[int(mapa) + 1]

    def UP(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.Y = self.Y-50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def DOWN(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.Y = self.Y+50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def RIGHT(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.X = self.X+50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def LEFT(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.X = self.X-50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def askfor(self,p1,p2,p3,p4,view):
        op=0
        #-----------------------------------------------------------------------
        for opc in range (1,4)
            if(opc==1):
                op=p1
            if(opc==2):
                op=p2
            if(opc==3):
                op=p3
            if(opc==4):
                op=p4
            #-------------------------------------------------------------------
            if(op==1):
                if(view.askLEFT(self.getX/50, self.getY/50) > "0"):
                    return "left"
            if(op==2):
                if(view.askUP(self.getX/50, self.getY/50) > "0"):
                    return "up"
            if(op==3):
                if(view.askRIGHT(self.getX/50, self.getY/50) > "0"):
                    return "right"
            if(op==4):
                if(view.askDOWN(self.getX/50, self.getY/50) > "0"):
                    return "down"
            return "false"


    #def choice(self):
