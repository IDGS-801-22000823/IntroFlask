from flask import Flask, render_template, request
import forms
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
from flask import g
from flask import flash
import zodiaco


app=Flask(__name__)
app.secret_key="key"
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request():
    g.user = "Mario"
    print ("before 1")

@app.after_request
def after_request(response):
    print ("before 3")
    return response

@app.route("/")
def index():
    titulo="IDS801"
    lista=["pedro","juan","luis"]
    nom=g.user
    print("Index 2 {}".format(g.user))
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "<h1>Hola, Mundo!</1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>Hola, {user}!</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El número es {n}!</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola,, {username} Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func(parm="juan"):
    return f"<h1>El parámetro es: {parm}</h1>"

@app.route("/aperas")
def aperas():
    return '''
    <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
    </form>
    '''
    
@app.route("/operas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET","POST"])
def result():
    n1=request.form["n1"]
    n2=request.form["n2"]
    return "La multiplicacion de {} x {} es {}".format(n1,n2,str(int(n1)*int(n2)))

@app.route("/operaciones", methods=["GET", "POST"])
def operaciones():
    resultado = ""
    if request.method == "POST":
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")
        if operacion == "suma":
            resultado = n1 + n2
        elif operacion == "resta":
            resultado = n1 - n2
        elif operacion == "multiplicacion":
            resultado = n1 * n2
        elif operacion == "division":
            if n2 != 0:
                resultado = n1 / n2
            else:
                resultado = "Error"
        else:
            resultado = "Nop"
    return render_template("OperasBas.html", resultado=resultado)

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    resultado = ""
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            compra = int(request.form["compra"])
            tarjeta = request.form["tarjeta"]
            boletos = int(request.form["boletos"])
            if compra <= 0 or boletos <= 0:
                resultado = "Como que 0 o menos ._.?"
            else:
                limite_boletos = compra * 7
                
                if boletos > limite_boletos:
                    resultado = f"No se pueden comprar mas de {limite_boletos} boletos para {compra} personas."
                else:
                    # Si hay descuento ZIP si no NOP
                    if boletos > 5:
                        descuento = 0.15
                    elif boletos >= 3:
                        descuento = 0.10
                    else:
                        descuento = 0

                    # tienes tarjeta vienestar de morena sjjsjsjs
                    if tarjeta == "si":
                        descuento += 0.10  # 10% adicional
                    # total
                    precio_boleto = 12
                    total_sin_descuento = boletos * precio_boleto
                    total_con_descuento = total_sin_descuento * (1 - descuento)

                    resultado = f"${total_con_descuento:.2f}"
        except ValueError:
            resultado = "Pero pon numeros."

    return render_template("cinepolis.html", resultado=resultado)

#ZODIACO CHINO
@app.route("/zodiacos", methods=["GET", "POST"])
def zodiacos():
    
    nombre = ""
    paterno = ""
    materno = ""
    edad = 0
    signo = ""
    imagen_zodiaco = ""

    zodiaco_clas = zodiaco.UserForm(request.form)

    if request.method == "POST" and zodiaco_clas.validate():

        nombre = zodiaco_clas.nombre.data
        paterno = zodiaco_clas.paterno.data
        materno = zodiaco_clas.materno.data
        dia = zodiaco_clas.dia.data
        mes = zodiaco_clas.mes.data
        anio = zodiaco_clas.anio.data

        mensaje = f"Gracias {nombre} por usar nuestra página ;3"
        flash(mensaje)

        # edad
        hoy = datetime.now()
        fecha_nacimiento = datetime(anio, mes, dia)
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        # signo zodiacal
        signos_chinos = ["mono", "gallo", "perro", "cerdo", "rata", "buey", "tigre", "conejo", "dragon", "serpiente", "caballo", "cabra"]
        indice = anio % 12
        signo = signos_chinos[indice]

        # Imagen
        imagen_zodiaco = f"{signo}.jpg"
        print(f"Signo: {signo}, Imagen: {imagen_zodiaco}")

    return render_template(
        "zodiacos.html",
        form=zodiaco_clas,
        nombre=nombre,
        paterno=paterno,
        materno=materno,
        edad=edad,
        signo=signo,
        imagen_zodiaco=imagen_zodiaco
    )

@app.route("/Alumnos", methods = ["GET" , "POST"])
def alumnos():
    mat = ''
    nom = ''
    ap = ''
    email = ''

    alumno_clas = forms.UserForm(request.form)
    if request.method == "POST" and alumno_clas.validate():
        mat = alumno_clas.mat.data
        nom = alumno_clas.nom.data
        ap = alumno_clas.ap.data
        email = alumno_clas.correo.data
        
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("Alumnos.html", form = alumno_clas, mat = mat, nom = nom, ap = ap, correo = email)


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)