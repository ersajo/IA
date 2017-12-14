from Arbol import *
class Character:

    tipo = ""
    distancia = 0
    costos = []
    costoT = 0
    X = 0
    Y = 0
    Tree=Arbol("0,0","0,0")

    def __init__(self, tipo, X, Y, costos):
        self.tipo = tipo
        self.X = X
        self.Y = Y
        self.Tree=Arbol(str(self.X/50)+","+str(self.Y/50),str(self.X/50)+","+str(self.Y/50))

        for i in range(len(costos)):
            if costos[i][0] == tipo:
                self.costos = costos[i]
                break

    def setX(self,X):
        self.X=X

    def setY(self,Y):
        self.Y=Y

    def setArbol(self):
        Tree=Arbol(str(self.X)+","+str(self.Y),str(self.X)+","+str(self.Y))

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
        print "estableciendo orden de prioridad"
        op=0
        aux=0
        priori=[" "," "," "," "," "]
        #-----------------------------------------------------------------------
        for opc in range (5):
            print priori
            if(opc==0):
                op=p1
            if(opc==1):
                op=p2
            if(opc==2):
                op=p3
            if(opc==3):
                op=p4

            if(op==1):
                priori[opc]="left"
                print "left"
                if(opc==4):
                    return priori
            if(op==2):
                priori[opc]="up"
                print "up"
                if(opc==4):
                    return priori
            if(op==3):
                priori[opc]="right"
                print "right"
                if(opc==4):
                    return priori
            if(op==4):
                priori[opc]="down"
                print "down"
                if(opc==4):
                    return priori

            #return "false"
