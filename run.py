from flask import Flask, render_template, request, flash, session, redirect
from flask_wtf.csrf import CSRFProtect
from historicos import Historico
from database import init_db, db_session
from models import Users, UsersForm, UserLoginForm, ImportExcel
from contar_variables import Contar
from manejo_archivos import Manejo_archivos
from manejo_validate import Manejo_validate
from sms_generico import Sms_generico
import pyexcel
import os
import datetime

from config import DevelopmentConfig

UPLOAD_FOLDER = os.path.abspath("../daniel25109")

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
csrf = CSRFProtect(app)

SECRET_KEY = 'CLAVE_SECRETA_VOXCALL2021'

init_db()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/users/register')
def user_register():
    if 'username' in session:
        return redirect('/calls/menu')

    form = UsersForm()
    return render_template('create.html', form = form)

@app.route('/users/save', methods=['POST'])
def user_save():
   form = UsersForm(request.form)
   if request.method == "POST":
         usuario = Users.query.filter(Users.username == form.username.data).first()
         if usuario == None:
            username = form.username.data
            password = form.password.data
            email = form.email.data

            usuario = Users(username, password, email)
            db_session.add(usuario)
            db_session.commit()

            session['username'] = usuario.username
            success_message = "Bienvenido "+usuario.username
            flash(success_message)

            return redirect('/calls/menu')
         else:
            success_message = "El usuario ya existe en el sistema"
            flash(success_message)
            form = UsersForm()
            return redirect('/users/register')

   else:
       return redirect('users/register')


@app.route('/')
@app.route('/users/login', methods=['GET','POST'])
def user_login():
   if 'username' in session:
       success_message = "Usuario ya logueado"
       flash(success_message)
       return redirect('/calls/menu')

   form = UserLoginForm(request.form)
   if request.method == "POST":
      user = Users.query.filter(Users.username == form.username.data).first()
      if user and user.check_password(form.password.data):
         session['username'] = user.username
         success_message = "Bienvenido "+user.username
         flash(success_message)

         return redirect('/calls/menu')
      else:
         success_message = "Usuario y/o contraseña incorrectos"
         flash(success_message)
         return render_template('login.html', form = form)
   else:
       return render_template('login.html', form = form)


@app.route('/users/logout')
def user_logout():
    if 'username' in session:
        session.pop('username')
        return redirect('/users/login')

@app.route('/calls/charge', methods=['POST'])
def cargar():
    if 'username' in session:
        if request.method == 'POST':
            tipo2 = request.form['type']
            archivo_lista = open("tipo.txt", "w")
            archivo_lista.write(tipo2)
            archivo_lista.close()
            tipo = request.form['tipo_2']
            try:
                int(tipo)
                return redirect('/calls/import/'+str(tipo))
            except:
                valores = request.form['tipo_2']
                elemento = Contar(valores)
                variables = elemento.contar()
                elemento.guardar_texto()

                return redirect('/calls/import/gene/'+str(len(variables)))
    else:
        return redirect('/users/login')

@app.route('/calls/menu')
def calls_menu():
    if 'username' in session:
        return render_template('menu.html')
    else:
        return redirect('/users/login')


@app.route('/calls/import/gene/<var>', methods=['GET', 'POST'])
def importar_gene(var):
    if 'username' in session:
        form = ImportExcel(request.form)
        if request.method=='POST':
            archivo = Manejo_archivos(request.files["archivo"])
            archivo.guardar()
            success_message = 'Tu archivo se ha guardado exitosamente'
            flash(success_message)
            cantidad = archivo.contar_lineas()
            leidos = pyexcel.get_sheet(file_name=archivo.archivo.filename, name_columns_by_row=0)
            return render_template("table.html", datos = leidos, cantidad = cantidad, tipo = "0", variables = var)
        else:
            return render_template('importar.html', form = form)
    else:
        return redirect('/users/login')


@app.route('/calls/import/<tipo>', methods=['GET', 'POST'])
def importar(tipo):
    if 'username' in session:
        form = ImportExcel(request.form)
        if request.method == 'POST':
            archivo = Manejo_archivos(request.files["archivo"])
            archivo.guardar()
            success_message = 'Tu archivo ha subido exitosamente'
            flash(success_message)
            cantidad = archivo.contar_lineas()
            leidos = pyexcel.get_sheet(file_name=archivo.archivo.filename, name_columns_by_row=0)

            return render_template('table.html', datos = leidos, cantidad=cantidad, tipo =tipo)
        else:
            return render_template('importar.html', form = form)
    else:
        return redirect('/users/login')

@app.route('/calls/validate', methods=['GET', 'POST'])
def calls_validate():
    if 'username' in session:
        if request.method == "POST":
            tipo = request.form['tipo']
            cantidad = request.form['cantidad']
            texto = open('tipo.txt', 'r')
            texto_leido = texto.read()
            texto.close()
            if texto_leido == 'call':
                elemento = Manejo_validate(tipo)
                elemento.calcular_cantidades(cantidad)
                elemento.filtro()
            elif texto_leido == "sms" and tipo == "0":
                cantidades = []
                for canti in cantidad:
                    if canti != "[" and canti != "]" and canti != "," and canti != " ":
                        canti = int(canti)
                        cantidades.append(canti)

                archivo = open("generico_bdd.txt", "w")
                for cantidad in cantidades:
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
                        for cantidad in cantidades:
                            contador = 0

                            for pos in lista_posiciones:
                                texto_posiciones[int(pos)] = request.form["variable_"+str(cantidad)+"_"+str(contador)]
                                contador = contador+1
                                str1=""
                            for elemento in texto_posiciones:
                                str1+=elemento+" "
                            archivo.write(str1+",\n")
                        archivo.close()

                        texto = open('texto_generico.txt', 'r')
                        texto_leido = texto.read()
                        texto.close()

                    else:
                        texto = open('texto_generico.txt', 'r')
                        texto_leido = texto.read()
                        texto_posiciones = texto_leido.split()
                        texto.close()
                          
                else:
                    texto = open('texto_generico.txt', 'r')
                    texto_leido = texto.read()
                    texto_posiciones = texto_leido.split()
                    texto.close()
                
                archivo = open("generico_bdd.txt")
                lineas = archivo.readlines()
                archivo.close()
                for linea in lineas:
                    elemento = Sms_generico(linea, texto_leido)
                    respuesta = elemento.envio()
            return redirect('/calls/menu')

    else:
        return redirect('/users/login')


@app.route('/contact', methods=['GET','POST'])
def contact():
    if 'username' in session:
        if request.method == 'POST':
            nombre = request.form["name"]
            print(nombre)
            return render_template('contact.html')
        else:
            if 'username' in session:
                return render_template('contact.html')
    else:
        login_form = forms.LoginForm(request.form)
        return render_template('index.html', form = login_form)

@app.route('/historic', methods=['GET','POST'])
def historico():
    if 'username' in session:
        if request.method == 'POST':
            inicio = request.form['fecha_inicio']
            final = request.form['fecha_final']

            f_inicio = datetime.datetime.strptime(inicio, "%Y-%m-%d")
            f_final = datetime.datetime.strptime(final, "%Y-%m-%d")

            archivo = open("historial_bdd.txt", "r")
            lineas = archivo.readlines()
            archivo.close()

            listado_cargar = []

            for linea in lineas:
                elemento = linea.split(",")
                f_elemento = datetime.datetime.strptime(elemento[0], "%Y-%m-%d")
                if elemento[1] == session['username']:
                    if f_elemento >= f_inicio and f_elemento <= f_final:
                        histo = Historico(elemento[0], elemento[2], elemento[3])
                        listado_cargar.append(histo)

            print(listado_cargar)
            return render_template('historico.html', listado = listado_cargar)
        else:
            listado_cargar = []
            return render_template('historico.html', listado = listado_cargar)
    else:
        login_form = forms.LoginForm(request.form)
        return render_template('index.html', form = login_form)

if __name__=='__main__':
    csrf.init_app(app)

    with app.app_context():
        app.run()