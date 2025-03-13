from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField,SubmitField
from wtforms import validators

class UserForm(Form):

    nombre = StringField("Nombre",[
        validators.DataRequired(message="El campo de nombre es requerido")
    ])
    paterno = StringField("Paterno",[
        validators.DataRequired(message="El campo de apellido paterno es requerido")
    ])
    materno = StringField("Materno",[
        validators.DataRequired(message="El campo de apellido materno es requerido")
    ])
    dia = IntegerField("Dia",[
        validators.DataRequired(message="El campo de dia es requerido")
    ])
    mes = IntegerField("Mes",[
        validators.DataRequired(message="El campo de mes es requerido")
    ])
    anio = IntegerField("Anio",[
        validators.DataRequired(message="El campo de año es requerido")
    ])