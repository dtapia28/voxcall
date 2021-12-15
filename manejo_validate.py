from call_generico import Generico
from flask import request, session
from call_bnc import Bnc_Credito, Bnc_Prdcto, Bnc_Cuota, Bnc_cambio
from call_comercial import Comercial_aumento, Comercial_producto, Comercial_cuota
from call_medico import Medico_hora, Medico_entrega
from models import Historico, Users
from datetime import datetime
from database import db_session
import json

class Manejo_validate():

    def __init__(self, tipo):
        self.tipo = tipo
        self.cantidades = []

    def calcular_cantidades(self,cantidad):
        for canti in cantidad:
            if canti != "[" and canti != "]" and canti != "," and canti != " ":
                canti = int(canti)
                self.cantidades.append(canti)

    def filtro(self):
            if self.tipo == "1":
                self.bnc_credito()
                self.llamada_bnc_credito()
            elif self.tipo == "2":
                self.bnc_producto()
                self.llamada_bnc_producto()
            elif self.tipo == "3":
                self.bnc_cuota()
                self.llamada_bnc_cuota()
            elif self.tipo == "4":
                self.bnc_cambio_clave()
                self.llamada_bnc_cambio_clave()
            elif self.tipo == "5":
                self.comercial_aumento()
                self.llamada_comercial_aumento()
            elif self.tipo == "6":
                self.comercial_producto()
                self.llamada_comercial_producto()
            elif self.tipo == "7":
                self.comercial_cuota()
                self.llamada_comercial_cuota()
            elif self.tipo == "8":
                self.medico_hora()
                self.llamada_medico_hora()
            elif self.tipo == "9":
                self.medico_entrega()
                self.llamada_medico_entrega()
            elif self.tipo == "0":
                self.generico()
                self.llamada_generico()

    def bnc_credito(self):
        archivo = open("banco_credito_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            banco = request.form["banco"+str(cantidad)]
            monto = request.form["monto"+str(cantidad)]
            fecha = request.form["fecha"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(banco+",")
            archivo.write(monto+",")
            archivo.write(fecha+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def bnc_producto(self):
        archivo = open("banco_producto_bdd.txt", "w")
        for cantidad in self.cantidades:
           nombre = request.form["nombre"+str(cantidad)]
           banco = request.form["banco"+str(cantidad)]
           opcion = request.form["opcion"+str(cantidad)]
           fecha = request.form["fecha"+str(cantidad)]
           telefono = request.form["phone"+str(cantidad)]

           archivo.write(nombre+",")
           archivo.write(banco+",")
           archivo.write(opcion+",")
           archivo.write(fecha+",")
           archivo.write(telefono+"\n")
        archivo.close()

    def bnc_cuota(self):
        archivo = open("banco_cuota_bdd.txt", "w")
        for cantidad in self.cantidades:
           nombre = request.form["nombre"+str(cantidad)]
           banco = request.form["banco"+str(cantidad)]
           monto = request.form["monto"+str(cantidad)]
           telefono = request.form["phone"+str(cantidad)]

           archivo.write(nombre+",")
           archivo.write(banco+",")
           archivo.write(monto+",")
           archivo.write(telefono+"\n")
        archivo.close()

    def bnc_cambio_clave(self):
        archivo = open("banco_cambio_clave_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            banco = request.form["banco"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(banco+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def comercial_aumento(self):
        archivo = open("comercial_aumento_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            casa_comercial = request.form["casa_comercial"+str(cantidad)]
            monto = request.form["monto"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(casa_comercial+",")
            archivo.write(monto+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def comercial_producto(self):
        archivo = open("comercial_producto_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            casa_comercial = request.form["casa_comercial"+str(cantidad)]
            producto = request.form["producto"+str(cantidad)]
            fecha = request.form["fecha"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(casa_comercial+",")
            archivo.write(producto+",")
            archivo.write(fecha+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def comercial_cuota(self):
        archivo = open("comercial_cuota_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            casa_comercial = request.form["casa_comercial"+str(cantidad)]
            monto = request.form["monto"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(casa_comercial+",")
            archivo.write(monto+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def medico_hora(self):
        archivo = open("medico_hora_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            fecha = request.form["fecha"+str(cantidad)]
            hora = request.form["hora"+str(cantidad)]
            medico = request.form["medico"+str(cantidad)]
            especialidad = request.form["especialidad"+str(cantidad)]
            centro = request.form["centro"+str(cantidad)]
            direccion = request.form["direccion"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(fecha+",")
            archivo.write(hora+",")
            archivo.write(medico+",")
            archivo.write(especialidad+",")
            archivo.write(centro+",")
            archivo.write(direccion+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def medico_entrega(self):
        archivo = open("medico_entrega_bdd.txt", "w")
        for cantidad in self.cantidades:
            nombre = request.form["nombre"+str(cantidad)]
            tipo_2 = request.form["tipo_2"+str(cantidad)]
            telefono = request.form["phone"+str(cantidad)]

            archivo.write(nombre+",")
            archivo.write(tipo_2+",")
            archivo.write(telefono+"\n")
        archivo.close()

    def generico(self):
        archivo = open("generico_bdd.txt", "w")
        for cantidad in self.cantidades:
            telefono = request.form["phone"+str(cantidad)]
            archivo.write(telefono+",\n")

        variables = int(request.form["variables"])
        archivo.close()

        if variables != None:
            if variables>0:
                texto = open('texto_generico.txt', 'r')
                texto_leido = texto.read()
                texto_posiciones = texto_leido.split()
                texto.close()

                posiciones = open('posicion_variables.txt', 'r')
                posiciones_lst = posiciones.read()
                lista_posiciones = posiciones_lst.split(',')
                del lista_posiciones[-1]

                archivo = open("texto_generico.txt", "w")
                for cantidad in self.cantidades:
                    contador = 0

                    for pos in lista_posiciones:
                        texto_posiciones[int(pos)] = request.form["variable_"+str(cantidad)+"_"+str(contador)]
                        contador = contador+1
                        str1=""
                    for elemento in texto_posiciones:
                        str1+=elemento+" "
                    archivo.write(str1+",\n")
                archivo.close()

    def llamada_bnc_credito(self):
        archivo = open("banco_credito_bdd.txt")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           banco = elemento[1]
           monto = elemento[2]
           fecha = elemento[3]
           telefono = elemento[4]

           llama = Bnc_Credito(nombre, banco, monto, fecha, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama


    def llamada_bnc_producto(self):
        archivo = open("banco_producto_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           banco = elemento[1]
           opcion = elemento[2]
           fecha = elemento[3]
           telefono = elemento[4]

           llama = Bnc_Prdcto(nombre, banco, opcion, fecha, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama



    def llamada_bnc_cuota(self):
        archivo = open("banco_cuota_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           banco = elemento[1]
           monto = elemento[2]
           telefono = elemento[3]

           llama = Bnc_Cuota(nombre, banco, monto, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama


    def llamada_bnc_cambio_clave(self):
        archivo = open("banco_cambio_clave_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           banco = elemento[1]
           telefono = elemento[2]

           llama = Bnc_cambio(nombre, banco, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama


    def llamada_comercial_aumento(self):
        archivo = open("comercial_aumento_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           casa_comercial = elemento[1]
           monto = elemento[2]
           telefono = elemento[3]

           llama = Comercial_aumento(nombre, casa_comercial, monto, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama
           resultado.guardar()

    def llamada_comercial_producto(self):
        archivo = open("comercial_producto_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           casa_comercial = elemento[1]
           producto = elemento[2]
           fecha = elemento[3]
           telefono = elemento[4]

           llama = Comercial_producto(nombre, casa_comercial, producto, fecha, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama

    def llamada_comercial_cuota(self):
        archivo = open("comercial_cuota_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
           elemento = linea.split(",")
           nombre = elemento[0]
           casa_comercial = elemento[1]
           monto = elemento[2]
           telefono = elemento[3]

           llama = Comercial_cuota(nombre, casa_comercial, monto, telefono)
           resultado = llama.llamada()
           resultado = json.loads(resultado)
           del llama


    def llamada_medico_hora(self):
        archivo = open("medico_hora_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            elemento = linea.split(",")
            nombre = elemento[0]
            fecha = elemento[1]
            hora = elemento[2]
            medico = elemento[3]
            especialidad = elemento[4]
            centro = elemento[5]
            direccion = elemento[6]
            telefono = elemento[7]

            llama = Medico_hora(nombre, fecha, hora, medico, especialidad, centro, direccion, telefono)
            resultado = llama.llamada()
            resultado = json.loads(resultado)
            del llama


    def llamada_medico_entrega(self):
        archivo = open("medico_entrega_bdd.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            elemento = linea.split(",")
            nombre = elemento[0]
            tipo_2 = elemento[1]
            telefono = elemento[2]

            llama = Medico_entrega(nombre, tipo_2, telefono)
            resultado = llama.llamada()
            resultado = json.loads(resultado)
            del llama


    def llamada_generico(self):
        print("Entra al metodo llamada_generico")
        variables = int(request.form["variables"])
        if variables == 0:
            archivo = open("generico_bdd.txt", "r")
            lineas = archivo.readlines()
            archivo.close()
            print("Carga archivo generico_txt")
            print(archivo)

            archivo_2 = open("texto_generico.txt", "r")
            texto = archivo_2.read()
            texto_lista = texto.split()
            archivo_2.close()
            print("Carga archivo texto_generico")
            print(archivo_2)

            for linea in lineas:
                elemento = linea.split(",")
                telefono = elemento[0]

                llama = Generico(texto, telefono)
                resultado = llama.llamada()
                resultado = json.loads(resultado)
                del llama
                tipo = "llamada"
                if tipo == "llamada":
                    monto = 0.09
                elif tipo == "sms":
                    monto = 0.22
                else:
                    monto = 0.0792    
               
                hoy = datetime.now();
                if 'username' in session:
                    user = session['username']
                    user = Users.query.filter_by(username=user).first()
                    resul = Historico(int(linea[0:11]), hoy, monto, tipo, user.id)
                    db_session.add(resul)
                    db_session.commit()               

        else:
            archivo = open("generico_bdd.txt", "r")
            lineas = archivo.readlines()
            archivo.close()

            archivo_2 = open("texto_generico.txt", "r")
            textos = archivo_2.readlines()

            contador = 0
            for linea in lineas:
                llama = Generico(textos[contador], int(linea[0:11]))
                resultado = llama.llamada()
                resultado = json.loads(resultado)
                print("Acá va el resultado")
                print(resultado)
                del llama
                tipo = "llamada"
                if tipo == "llamada":
                    monto = 0.09
                elif tipo == "sms":
                    monto = 0.22
                else:
                    monto = 0.0792    
               
                hoy = datetime.now();
                if 'username' in session:
                    user = session['username']
                    user = Users.query.filter_by(username=user).first()
                    resul = Historico(int(linea[0:11]), hoy, monto, tipo, user.id)
                    db_session.add(resul)
                    db_session.commit() 
                    contador = contador+1
