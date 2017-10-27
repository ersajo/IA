class Archivo:

    def read(self, ruta):
        with open(ruta, 'r') as leer:
            contenido = leer.read().split('\n')
        i = 0
        for line in contenido:
            contenido[i] = line.split(',')
            i = i + 1
        return contenido
