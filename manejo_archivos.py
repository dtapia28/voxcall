import os
import pyexcel

class Manejo_archivos():

    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self):
        archivo = self.archivo
        nombre = archivo.filename
        archivo.save(os.path.join("../voxcall", nombre))

    def contar_lineas(self):
        leidos = pyexcel.get_sheet(file_name = self.archivo.filename, name_columns_by_row=0)
        cantidad_lineas = []
        contador = 0
        for leido in leidos:
            cantidad_lineas.append(contador)
            contador = contador+1
        return cantidad_lineas