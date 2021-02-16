class Contar():

    def __init__(self, valores):
        self.valores = valores

    def contar(self):

        contador = 0
        variables = []

        for letra in self.valores:
            if letra == '{':
                variables.append(contador)
            if letra == " ":
                contador = contador+1

        return variables

    def guardar_texto(self):
        archivo_lista = open("texto_generico.txt", "w")
        archivo_lista.write(self.valores)
        archivo_lista.close()
        archivo = open("posicion_variables.txt", "w")
        for num in self.contar():
           archivo.write(str(num)+",")
        archivo.close    
