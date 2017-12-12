from Character import *
from Escenario import *

class Search:

    def __init__(self):

    #---------------------------------------------------------------------------
    def BusquedaProfundidad(self, X, Y, World,p1,p2,p3,p4):
        askfor(p1,p2,p3,p4)



    def BusquedaAnchura(self, X, Y, WORLD,p1,p2,p3,p4):
        askfor(p1,p2,p3,p4)


    def askfor():
        op=0
        #-----------------------------------------------------------------------
        for opc in range (0,4)
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
                if(view.askLEFT(monito.getX/50, monito.getY/50) > "0"):
                    return "left"
            if(op==2):
                if(view.askUP(monito.getX/50, monito.getY/50) > "0"):
                    return "up"
            if(op==3):
                if(view.askRIGHT(monito.getX/50, monito.getY/50) > "0"):
                    return "right"
            if(op==4):
                if(view.askDOWN(monito.getX/50, monito.getY/50) > "0"):
                    return "down"
            return "false"
