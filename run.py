from flask import Flask, render_template, request, flash, session, redirect
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.sql.expression import false
from database import init_db, db_session
from models import Users, UsersForm, UserLoginForm, ImportExcel, Historico, Roles, UserChangePassword
from contar_variables import Contar
from manejo_archivos import Manejo_archivos
from manejo_validate import Manejo_validate
from sms_generico import Sms_generico
from envia_whatsapp import Envio_whatsapp
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_migrate import Migrate
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

db = init_db()

migrate = Migrate(app, db)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/users')
def users():
    if 'username' in session:
        usuario = Users.query.filter(Users.username == session['username']).first()
        if usuario.rol != 1:
            return redirect('/menu')
        else:
            users = Users.query.filter(Users.rol != 1).all()
            nombre_vista = "Usuarios"
            titulo_vista = "Voxcall - Usuarios"
            return render_template('users2.html', users=users, usuario=usuario, nombre_vista = nombre_vista, titulo_vista = titulo_vista)
            
@app.route('/users/register')
def user_register():
    if 'username' in session:
        usuario = Users.query.filter(Users.username == session['username']).first()
        if usuario.rol != 1:
            return redirect('/menu')
        else:    
            roles = Roles.query.all()
            return render_template('create.html', data=roles)

@app.route('/users/save', methods=['POST'])
def user_save():
   form = UsersForm(request.form)
   if request.method == "POST":
        usuario = Users.query.filter(Users.username == form.username.data).first()
        if usuario == None:
            username = form.username.data
            password = form.password.data
            email = form.email.data
            rol = form.rol.data

            usuario = Users(username, password, email, rol)
            db_session.add(usuario)
            db_session.commit()

            if 'username' in session:
                usuario = Users.query.filter(Users.username == session['username']).first()
                if usuario.rol == 1:
                    success_message = "Usuario creado correctamente"
                    return redirect('/menu')
        else:
            success_message = "El usuario ya existe en el sistema"
            flash(success_message)
            form = UsersForm()
            return redirect('/users/register')

   else:
       return redirect('users/register')


@app.route("/users/delete/<int:id>")
def user_delete(id:int):
    if 'username' in session:
        usuario = Users.query.filter(Users.username == session['username']).first()
        if usuario.rol != 1:
            return redirect('/menu')
        else:
            usuario = Users.query.filter(Users.id == id).first()
            db_session.delete(usuario)
            db_session.commit()

            return redirect('/users')

@app.route('/users/edit/<int:id>', methods=['GET','POST'])
def user_edit(id:int):
    if request.method == "GET":
        if 'username' in session:
            usuario = Users.query.filter(Users.id == id).first()
            user = Users.query.filter(Users.username == session['username']).first()
            roles = Roles.query.all()

            return render_template('edit.html', usuario=usuario, roles=roles, user=user)

    elif request.method == 'POST':
        form = UsersForm(request.form)
        usuario = Users.query.filter(Users.id == id).first()
        user = Users.query.filter(Users.username == session['username']).first()

        if form.username.data != "" and form.username.data != usuario.username:
            usuario.username = form.username.data

        if form.email.data != "" and form.email.data != usuario.email:
            usuario.email = form.email.data
        

        if form.password.data != "" and generate_password_hash(form.password.data) != usuario.passwordhash:
            usuario.passwordhash = generate_password_hash(form.password.data)
            if user.rol == 1:
                if usuario.cambio_clave == True:
                    usuario.cambio_clave = False

        db_session.commit()

        if user.rol == 1:
            return redirect('/users')
        else:
            return redirect('/menu')


@app.route('/')
@app.route('/users/login', methods=['GET','POST'])
def user_login():
   if 'username' in session:
       success_message = "Usuario ya logueado"
       flash(success_message)
       return redirect('/menu')

   if request.method == "POST":
      user = Users.query.filter(Users.username == request.form['username']).first()
      if user and user.check_password(request.form['password']):
         session['username'] = user.username
         success_message = "Bienvenido "+user.username
         if user.cambio_clave == True:
            flash(success_message)    

         return redirect('/menu')
      else:
         success_message = "Usuario y/o contraseña incorrectos"
         flash(success_message)
         return render_template('login.html')
   else:
       return render_template('login.html')

@app.route('/users/change_password', methods=['GET','POST'])
def change_password():
    if 'username' in session:
        if request.method == "GET":
            flash("Es necesario el cambio de contraseña.", 'warning')
            return render_template('change_password.html')
        elif request.method == "POST":
            form = UserChangePassword(request.form)
            user = Users.query.filter(Users.username == session['username']).first()
            password = form.password.data
            password_repite = form.password_repite.data

            if password == password_repite:
                user.password = generate_password_hash(password)
                user.cambio_clave = True
                db_session.commit()
                flash("Contraseña cambiada exitosamente")
                return redirect('/menu')
            else:
                flash("Contraseñas no son iguales")
                return render_template('change_password.html')
    else:
        return redirect('/users/login')       

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

@app.route('/menu')
def calls_menu():
    if 'username' in session:
        usuario = Users.query.filter_by(username=session['username']).first()
        if usuario.cambio_clave == False:
            
            return redirect('users/change_password')
        else:
            nombre_vista = "Inicio"
            titulo_vista = "Voxcall - Menú"

            return render_template('index.html', usuario = usuario, nombre_vista = nombre_vista, titulo_vista = titulo_vista)      
    else:
        return redirect('/users/login')

@app.route('/historico')
def cargar_historico():
    if 'username' in session:
        if request.method == 'GET':
            user = session['username']
            user = Users.query.filter_by(username=user).first()
            data = Historico.query.filter_by(user_id = user.id).all()
            usuario = Users.query.filter_by(username=session['username']).first()
            nombre_vista = "Histórico"
            titulo_vista = "Voxcall - Histórico"            

            return render_template('historico.html', datos = data, usuario=usuario, nombre_vista = nombre_vista, titulo_vista=titulo_vista)
        else:
            return redirect('/menu')
    else:
        return redirect('/users/login')


@app.route('/calls/import/gene/<var>', methods=['GET', 'POST'])
def importar_gene(var):
    if 'username' in session:
        if request.method=='POST':
            archivo = Manejo_archivos(request.files["archivo"])
            archivo.guardar()
            success_message = 'Tu archivo se ha guardado exitosamente'
            flash(success_message)
            cantidad = archivo.contar_lineas()
            cantidad_ultima = cantidad[-1]
            leidos = pyexcel.get_sheet(file_name=archivo.archivo.filename, name_columns_by_row=0)
            return render_template("table2.html", datos = leidos, cantidad = cantidad, tipo = "0", variables = var, ultima = cantidad_ultima)
        else:
            return render_template('importar.html')
    else:
        return redirect('/users/login')


@app.route('/calls/import/<tipo>', methods=['GET', 'POST'])
def importar(tipo):
    if 'username' in session:
        if request.method == 'POST':
            archivo = Manejo_archivos(request.files["archivo"])
            archivo.guardar()
            success_message = 'Tu archivo ha subido exitosamente'
            flash(success_message)
            cantidad = archivo.contar_lineas()
            leidos = pyexcel.get_sheet(file_name=archivo.archivo.filename, name_columns_by_row=0)
            cantidad_ultima = cantidad[-1]
            return render_template('table2.html', datos = leidos, cantidad=cantidad, tipo =tipo, ultima = cantidad_ultima)
        else:
            return render_template('importar.html')
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

            ## Modo llamada
            if texto_leido == 'call':
                elemento = Manejo_validate(tipo)
                elemento.calcular_cantidades(cantidad)
                elemento.filtro()

            ## Modo SMS
            elif texto_leido == "sms" and tipo == "0":
                cantidades = []
                for canti in cantidad:
                    if canti != "[" and canti != "]" and canti != "," and canti != " ":
                        canti = int(canti)
                        cantidades.append(canti)

                archivo = open("generico_bdd.txt", "w")
                for cantidad in cantidades:
                    telefono = request.form["phone"+str(cantidad)]
                    archivo.write(telefono+", \n")

                variables = int(request.form["variables"])
                archivo.close()

                if variables != None:

                    if variables>0:
                        print("SMS con variable mayor a 0")
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
                        texto_posiciones = texto_leido.split(',')
                        texto.close()

                        archivo = open("generico_bdd.txt")
                        lineas = archivo.readlines()
                        archivo.close()
                        for num in range(len(lineas)):
                            print(num)
                            elemento = Sms_generico(lineas[num], texto_posiciones[num])
                            respuesta = elemento.envio()
                            tipo = "sms"
                            if tipo == "llamada":
                                monto = 0.09
                            elif tipo == "sms":
                                monto = 0.22
                            else:
                                monto = 0.0792    
                        
                            hoy = datetime.now()
                            if 'username' in session:
                                user = session['username']
                                user = Users.query.filter_by(username=user).first()
                                resul = Historico(lineas[num], hoy, monto, tipo, user.id)
                                db_session.add(resul)
                                db_session.commit()


                    else:
                        print("SMS con variable 0")
                        texto = open('texto_generico.txt', 'r')
                        texto_leido = texto.read()
                        texto.close()

                        archivo = open("generico_bdd.txt")
                        lineas = archivo.readlines()
                        archivo.close()
                        for num in range(len(lineas)):
                            print(num)
                            elemento = Sms_generico(lineas[num], texto_leido)
                            respuesta = elemento.envio()
                            tipo = "sms"
                            if tipo == "llamada":
                                monto = 0.09
                            elif tipo == "sms":
                                monto = 0.22
                            else:
                                monto = 0.0792    
                        
                            hoy = datetime.datetime.now()
                            if 'username' in session:
                                user = session['username']
                                user = Users.query.filter_by(username=user).first()
                                resul = Historico(lineas[num], hoy, monto, tipo, user.id)
                                db_session.add(resul)
                                db_session.commit()                            

                else:
                    print("SMS sin variable")
                    texto = open('texto_generico.txt', 'r')
                    texto_leido = texto.read()
                    texto.close()

                    archivo = open("generico_bdd.txt")
                    lineas = archivo.readlines()
                    archivo.close()
                    for linea in lineas:
                        elemento = Sms_generico(linea, texto_leido)
                        respuesta = elemento.envio()
                        tipo = "sms"
                        if tipo == "llamada":
                            monto = 0.09
                        elif tipo == "sms":
                            monto = 0.22
                        else:
                            monto = 0.0792    
                        
                        hoy = datetime.now()
                        if 'username' in session:
                            user = session['username']
                            user = Users.query.filter_by(username=user).first()
                            resul = Historico(linea, hoy, monto, tipo, user.id)
                            db_session.add(resul)
                            db_session.commit()          
            
            
            elif texto_leido == "whatsapp" and tipo == "0":
                elemento = Envio_whatsapp()
                con = elemento.conexion()
                cantidades = []
                for canti in cantidad:
                    if canti != "[" and canti != "]" and canti != "," and canti != " ":
                        canti = int(canti)
                        cantidades.append(canti)

                archivo = open("generico_bdd.txt", "w")
                for cantidad in cantidades:
                    telefono = request.form["phone"+str(cantidad)]
                    archivo.write(telefono+", \n")

                variables = int(request.form["variables"])
                archivo.close()

                print("Las variables son: "+str(variables))
                if variables != 0:

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
                        texto_posiciones = texto_leido.split(',')
                        texto.close()

                        archivo = open("generico_bdd.txt")
                        lineas = archivo.readlines()
                        archivo.close()
                        for num in range(len(lineas)):
                            print(num)

                else:
                    texto = open('texto_generico.txt', 'r')
                    texto_leido = texto.read()
                    texto.close()

                    archivo = open("generico_bdd.txt")
                    lineas = archivo.readlines()
                    archivo.close()
                    
                    for linea in lineas:
                        elemento.envio(con)                    
                    

            return redirect('/menu')

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
    migrate.init_app(app, db)
    csrf.init_app(app)

    with app.app_context():
        app.run()