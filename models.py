from sqlalchemy import Column, BigInteger, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, validators, FileField
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField

class Users(Base):
    __tablename__='users'
    id = Column(BigInteger, primary_key = True)
    username = Column(String(50), nullable=False, unique=True)
    passwordhash = Column(String(300), nullable=False)
    email = Column(String(60), nullable=False)
    create_at = Column(DateTime, default=datetime.datetime.utcnow)
    llamada = relationship("Llamadas")

    def __init__(self, username, passwordhash, email):
        self.username = username
        self.email = email
        self.passwordhash = generate_password_hash(passwordhash)

    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)


class UsersForm(FlaskForm):
    username = StringField('Usuario', [validators.Required()])
    password = PasswordField('Contraseña', [validators.Required()])
    email = EmailField('Email', [validators.Required()])

class UserLoginForm(FlaskForm):
    username = StringField('Usuario', [validators.Required()])
    password = PasswordField('Contraseña', [validators.Required()])

from wtforms import Form

class ImportExcel(Form):
    style={'class':'title_import'}
    archivo = FileField(u'Seleccionar archivo',
            [validators.required()],
            render_kw=style)


class Llamadas(Base):
    __tablename__='llamadas'
    id = Column(BigInteger, primary_key = True)
    numero = Column(String(15), nullable=False)
    fecha = Column(Date, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'))

    def __init__(self, numero, fecha, user_id):
        self.numero = numero
        self.fecha = fecha
        self.user_id = user_id