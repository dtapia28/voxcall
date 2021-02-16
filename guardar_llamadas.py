from flask import session
import datetime
class Guardar_llamadas():

    def __init__(self, resultado, telefono, tipo):
        self.resultado = resultado
        self.telefono = telefono
        self.tipo = tipo

    def guardar(self):
        if self.resultado['success'] == True and self.resultado['result'] == True:
            fecha = datetime.datetime.now()
            fecha = fecha.strftime("%Y-%m-%d")
            archivo_lista = open("historial_bdd.txt", "a")
            archivo_lista.write(fecha+",")
            nombre = session['username']
            archivo_lista.write(nombre+",")
            archivo_lista.write(str(self.tipo)+",")
            archivo_lista.write(str(self.telefono)+"\n")
            archivo_lista.close()