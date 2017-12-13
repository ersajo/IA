from tkinter import *
from genlib import *

class GUI:

    def __init__(self):
        self.master = Tk()
        self.master.geometry('500x200')
        self.master.title("Algoritmos Geneticos")

        MODES = [
            ("Funcion1", 1),
            ("Funcion2", 2),
            ("Funcion3", 3),
            ("Funcion4", 4),
            ("Funcion5", 5)
        ]

        self.var = IntVar()

        Label(self.master, text=" ").grid(column=0,row=0)
        i = 1
        for text, mode in MODES:
            Radiobutton(self.master, text=text, variable=self.var, value=mode, indicatoron=0).grid(column=1,row=i)
            i = i + 1
        Label(self.master, text=" ").grid(column=2)

        self.botonEjecutar = Button(self.master, text="Ejecutar", width=10, command=self.ejecutar).grid(row=3, column=3)
        #self.botonImprimir = Button(self.master, text="Imprimir en consola", width=15, command=self.callback).grid(row=4, column=3)
        self.variable = IntVar()
        self.variable.set(None)
        Radiobutton(self.master, text="Maximizar", variable=self.variable, value=1, indicatoron=0).grid(column = 3, row=1)
        Radiobutton(self.master, text="Minimizar", variable=self.variable, value=0, indicatoron=0).grid(column = 3, row=2)

        Label(self.master, text=" ").grid(column=4)

        Label(self.master, text="Numero de individuos").grid(column=5, row=1, sticky=E)
        Label(self.master, text="Numero de generaciones").grid(column=5, row=2, sticky=E)
        Label(self.master, text="Intervalo").grid(column=5, row=3, sticky=E)

        self.individuos = Entry(self.master, width=5)
        self.individuos.grid(column=6, row=1)
        self.generaciones = Entry(self.master, width=5)
        self.generaciones.grid(column=6, row=2)
        self.intervaloMin = Entry(self.master, width=5)
        self.intervaloMin.grid(column=6, row=3)
        Label(self.master, text="a").grid(column=7, row=3)
        self.intervaloMax = Entry(self.master, width=5)
        self.intervaloMax.grid(column=8, row=3)

    def ejecutar(self):
        i = int(self.individuos.get())
        imin = int(self.intervaloMin.get())
        imax = int(self.intervaloMax.get())
        g = Genetico(i, imin, imax)
        indices = g.eval(self.var.get(),self.variable.get(), 0)
        g.cross(indices, i, 0)
        for j in range(int(self.generaciones.get()) + 1):
            indices = g.eval(self.var.get(), self.variable.get(), j)
            g.cross(indices, i, j)
            print(g.getIndividuos(j))
        print("")

    def callback(self):
        print("Individuos= {}\nGeneraciones= {}\nIntervalo de {} a {}".format(self.individuos.get(), self.generaciones.get(), self.intervaloMin.get(), self.intervaloMax.get()))
