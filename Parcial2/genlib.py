import numpy as np
import matplotlib.pyplot as plt

"""
Representacion:     Se tiene un arreglo de longitud n donde xi es el valor de x
Evaluacion:         Se usaran las funciones dadas en el documento 2P Genetics algorithms Lab Practice 1.doc y se elegiran
                    de acuerdo al criterio de minimizar/maximizar se optaran por las que tengan un mejor resultado tomando
                    la mitad de los resultados para sobrevivir a la siguiente generacion.
Cruzamiento:        Se transformara el valor xi en una cadena binaria representando el valor dado y utilizando un
                    cruzamiento de un punto aleatorio se procedera a seleccionar los hijos aptos a sobrevivir de
                    acuerdo con las restricciones; Si al realizar los cruzamientos, no se generan los hijos suficientes
                    se introduce "sangre nueva"
Mutacion:           Se realizara una mutacion en un bit aleatorio en un individuo aleatorio en una generacion aleatoria 
                    dentro de las establecidas por el usuario, donde el bit seleccionado sera seteado a su inverso
Restricciones:      *Los individuos en cada generacion tienen que estar dentro del intervalo X 
                    *Si se detecta una division por 0 se introduce sangre nueva
"""

class Genetico:

    def __init__(self, individuos, imin, imax):
        self.generacion = []
        self.generacion.append(np.random.randint(imin, high=imax, size=individuos))
        self.min = imin
        self.max = imax
        self.ind = individuos

    def plot(self, flag, generaciones):
        y = []
        yi = []
        xi =[]
        for num in range(self.max):
            if num == 30 or num == 50 or num == 80:
                pass
            else:
                xi.append(num)
        color = []
        if flag == 1:  # x**2
            for valor in xi:
                yi.append(valor ** 2)
        elif flag == 2:  # sinx * 40
            for valor in xi:
                yi.append(np.sin(valor) * 40)
        elif flag == 3:  # cosx + x
            for valor in xi:
                yi.append(np.cos(valor) + valor)
        elif flag == 4:  # (1000/|50-x|)+x
            for valor in xi:
                yi.append(((1000 / np.absolute(50 - valor)) + valor))
        elif flag == 5:  # (1000/|30-x|)+(1000/|50-x|)+(1000/|80-x|)+x
            for valor in xi:
                res = (1000 / np.absolute(30 - valor)) + (1000 / np.absolute(50 - valor)) + (1000 / np.absolute(80 - valor)) + valor
                yi.append(res)
        plt.plot(xi, yi, alpha = 0.3)
        for gen in range(generaciones + 1):
            color.append(np.random.rand(self.ind))
            y.append([])
            if flag == 1:  # x**2
                for valor in self.generacion[gen]:
                    y[gen].append(valor ** 2)
            elif flag == 2:  # sinx * 40
                for valor in self.generacion[gen]:
                    y[gen].append(np.sin(valor) * 40)
            elif flag == 3:  # cosx + x
                for valor in self.generacion[gen]:
                    y[gen].append(np.cos(valor) + valor)
            elif flag == 4:  # (1000/|50-x|)+x
                for valor in self.generacion[gen]:
                    y[gen].append((1000 / np.absolute(50 - valor) + valor))
            elif flag == 5:  # (1000/|30-x|)+(1000/|50-x|)+(1000/|80-x|)+x
                for valor in self.generacion[gen]:
                    res = (1000 / np.absolute(30 - valor)) + (1000 / np.absolute(50 - valor)) + (1000 / np.absolute(80 - valor)) + valor
                    y[gen].append(res)
            plt.scatter(self.generacion[gen], y[gen], c=color[gen], alpha=0.5)
        plt.show()

    def getIndividuos(self,gen):
        return self.generacion[gen]

    def eval(self, flag, objetivo, gen):
        eval = []
        if flag == 1:#x**2
            for valor in self.generacion[gen]:
                eval.append(valor**2)
        elif flag == 2:#sinx * 40
            for valor in self.generacion[gen]:
                eval.append(np.sin(valor) * 40)
        elif flag == 3:#cosx + x
            for valor in self.generacion[gen]:
                eval.append(np.cos(valor) + valor)
        elif flag == 4:#(1000/|50-x|)+x
            i = 0
            for valor in self.generacion[gen]:
                while valor == 50:
                    valor = np.random.randint(self.min, high=self.max)
                    self.generacion[gen][i] = valor
                eval.append(((1000/np.absolute(50 - valor)) + valor))
                i = i + 1
        elif flag == 5:#(1000/|30-x|)+(1000/|50-x|)+(1000/|80-x|)+x
            i = 0
            for valor in self.generacion[gen]:
                while valor == 30 or valor == 50 or valor == 80:
                    valor = np.random.randint(self.min, high=self.max)
                    self.generacion[gen][i] = valor
                res = (1000/np.absolute(30 - valor)) + (1000/np.absolute(50 - valor)) + (1000/np.absolute(80 - valor)) + valor
                eval.append(res)
                i = i + 1
        out = []
        i=0
        if objetivo == 0:#Minimizar
            evalsort = sorted(eval)
        elif objetivo == 1:#Maximizar
            evalsort = sorted(eval,reverse=True)
        while len(out) != len(eval)//2:
            for num in range(len(evalsort)):
                if evalsort[i] == eval[num] and not(num in out):
                    out.append(num)
                    break
            i = i + 1
        return out

    def cross(self, survivors, tamaño, gen, obj):
        rand = np.random.randint(3, high=len(bin(self.max)))
        individuos = []
        for val in survivors:
            individuos.append(self.generacion[gen][val])
        binarios = []
        for survivor in survivors:
            s = bin(self.generacion[gen][survivor])
            if len(s) != len(bin(self.max)):
                s = s[:2] + '0'*(len(bin(self.max)) - len(s)) + s[2:]
            binarios.append(s)
        hijos = []
        for num in range(len(binarios)-1):
            p1 = binarios[num]
            for i in range(num+1,len(binarios)):
                p2 = binarios[i]
                children1 = p1[:rand] + p2[rand:]
                children2 = p2[:rand] + p1[rand:]
                hijos.append(children1)
                hijos.append(children2)
        for hijo in hijos:
            if int(hijo, 2) > self.max and obj == 1:
                pass
            elif int(hijo, 2) < self.min and obj == 0:
                pass
            else:
                individuos.append(int(hijo,2))
        while len(individuos) != tamaño:
            if len(individuos) < tamaño:
                individuos.append(np.random.randint(self.min, high=self.max))
            elif len(individuos) > tamaño:
                individuos.pop(len(individuos)-1)
        self.generacion.append(individuos)

    def mutation(self, indice):
        individuos = self.generacion[indice]
        rInd = np.random.randint(len(individuos))
        choosen = self.generacion[indice][rInd]
        choosen = bin(choosen)
        if len(choosen) != len(bin(self.max)):
            choosen = choosen[:2] + '0' * (len(bin(self.max)) - len(choosen)) + choosen[2:]
        rBit = np.random.randint(3,high=len(choosen))
        if choosen[rBit] == '0':
            choosen = choosen[:rBit] + '1' + choosen[rBit+1:]
        elif choosen[rBit] == '1':
            choosen = choosen[:rBit] + '0' + choosen[rBit+1:]
        if int(choosen,2) > self.max:
            choosen = bin(self.max)
        if int(choosen,2) < self.min:
            choosen = bin(self.min)
        print(int(choosen,2),rInd)
        self.generacion[indice][rInd] = int(choosen,2)