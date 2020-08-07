from wtforms import Form, validators
from wtforms import StringField, TextField, FileField
from wtforms.fields import PasswordField
from wtforms.fields import Field

class LoginForm(Form):
    username = StringField(u'Usuario',
                [
                    validators.required(), validators.length(min=5, message="Ingrese un usuario valido")
                ])
    password = PasswordField(u'Contraseña',[validators.required(), validators.length(min=5, message="Ingrese una contraseña valida")])

class ImportExcel(Form):
    style={'class':'title_import'}
    archivo = FileField(u'Seleccionar archivo',
            [validators.required()],
            render_kw=style)