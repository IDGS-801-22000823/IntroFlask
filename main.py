from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    titulo="IDS801"
    lista=["pedro","juan","luis"]
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



if __name__ == "__main__":
    app.run(debug=True, port=3000)