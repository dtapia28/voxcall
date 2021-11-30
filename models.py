from sqlalchemy import Column, BigInteger, String, DateTime, Date, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from flask_user import UserMixin
from database import Base
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from wtforms import Form

from flask_wtf import FlaskForm
from wtforms import StringField, validators, FileField
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField

class Users(Base, UserMixin):
    __tablename__='users'
    id = Column(BigInteger, primary_key = True)
    estado = Column('is_active', Boolean, nullable=False, server_default="1")
    username = Column(String(50, collation='NOCASE'), nullable=False, unique=True)
    passwordhash = Column(String(300), nullable=False, server_default='')
    email = Column(String(60), nullable=False)
    create_at = Column(DateTime, default=datetime.datetime.utcnow)
    llamada = relationship("Historico")

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


class ImportExcel(Form):
    style={'class':'title_import'}
    archivo = FileField(u'Seleccionar archivo',
            [validators.required()],
            render_kw=style)


class Historico(Base):
    __tablename__='historico'
    id = Column(BigInteger, primary_key = True)
    numero = Column(String(15), nullable=False)
    fecha = Column(Date, nullable=False)
    monto = Column(Float,nullable=False)
    tipo = Column(String(15), nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'))

    def __init__(self, numero, fecha, monto, tipo, user_id):
        self.numero = numero
        self.fecha = fecha
        self.monto = monto
        self.tipo = tipo
        self.user_id = user_id