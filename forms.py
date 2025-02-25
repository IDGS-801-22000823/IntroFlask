from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField,SubmitField
from wtforms import validators

class UserForm(Form):

    mat = IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido")
    ])
    nom = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    ap = StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])