from tkinter import *


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

        var = IntVar()
        var.set(1)

        i = 0
        for text, mode in MODES:
            Radiobutton(self.master, text=text, variable=var, value=mode, indicatoron=0).grid(row=i)
            i = i + 1

        Label(self.master, text=" ").grid(column=1)

        variable = IntVar()
        Radiobutton(self.master, text="Maximizar", variable=variable, value=1, indicatoron=0).grid(column = 2, row=0)
        Radiobutton(self.master, text="Minimizar", variable=variable, value=0, indicatoron=0).grid(column = 2, row=1)

        Label(self.master, text=" ").grid(column=3)

        Label(self.master, text="Numero de individuos").grid(column=4, row=0, sticky=E)
        Label(self.master, text="Numero de generaciones").grid(column=4, row=1, sticky=E)
        Label(self.master, text="Intervalo").grid(column=4, row=2, sticky=E)

        self.individuos = Entry(self.master, width=5)
        self.individuos.grid(column=5, row=0)
        self.generaciones = Entry(self.master, width=5)
        self.generaciones.grid(column=5, row=1)
        self.intervaloMin = Entry(self.master, width=5)
        self.intervaloMin.grid(column=5, row=2)
        Label(self.master, text="a").grid(column=6, row=2)
        self.intervaloMax = Entry(self.master, width=5)
        self.intervaloMax.grid(column=7, row=2)

        self.botonImprimir = Button(self.master, text="Imprimir en consola", width=15, command=self.callback).grid(row=5, column=0)

    def callback(self):
        print("Individuos= {}\nGeneraciones= {}\nIntervalo de {} a {}".format(self.individuos.get(), self.generaciones.get(), self.intervaloMin.get(), self.intervaloMax.get()))




gui = GUI()
mainloop()