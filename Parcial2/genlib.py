import numpy as np

"""
Representacion:     Se tiene un arreglo de longitud n donde xi es el valor de x
Evaluacion:         Se usaran las funciones dadas en el documento 2P Genetics algorithms Lab Practice 1.doc y se elegiran
                    de acuerdo al criterio de minimizar/maximizar se optaran por las que tengan un mejor resultado tomando
                    la mitad de los resultados para sobrevivir a la siguiente generacion.
Cruzamiento:        Se transformara el valor xi en una cadena binaria representando el valor dado y utilizando un
                    cruzamiento de un punto aleatorio se procedera a seleccionar los hijos aptos a sobrevivir de
                    acuerdo con las restricciones; Si al realizar los cruzamientos, no se generan los hijos suficientes
                    se introduce "sangre nueva"
Mutacion:           Se realizara una mutacion en un bit aleatorio en un generacion aleatoria dentro de las establecidas
                    por el usuario, donde el bit seleccionado sera seteado a su inverso
Restricciones:      Los individuos en cada generacion tienen que estar dentro del intervalo X 
"""

class Genetico:

    def __init__(self, individuos, imin, imax):
        self.generacion = []
        self.generacion.append(np.random.randint(imin, high=imax, size=individuos))
        self.min = imin
        self.max = imax

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
            for valor in self.generacion[gen]:
                eval.append((1000/np.absolute(50 - valor) + valor))
        elif flag == 5:#(1000/|30-x|)+(1000/|50-x|)+(1000/|80-x|)+x
            for valor in self.generacion[gen]:
                res = (1000/np.absolute(30 - valor)) + (1000/np.absolute(50 - valor)) + (1000/np.absolute(80 - valor)) + valor
                eval.append(res)
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

    def cross(self, survivors, tamaño, gen):
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
            if int(hijo, 2) > self.max:
                pass
            else:
                individuos.append(int(hijo,2))
        while len(individuos) != tamaño:
            if len(individuos) < tamaño:
                individuos.append(np.random.randint(self.min, high=self.max))
            elif len(individuos) > tamaño:
                individuos.pop(len(individuos)-1)
        self.generacion.append(individuos)

    def mutation(self):
        print("")
