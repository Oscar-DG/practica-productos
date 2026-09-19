
# IMPORTACIONES

from flask import Flask, render_template


# CONFIGURACION GENERAL

app = Flask(__name__)

# Clave necesaria para utilizar mensajes flash más adelante
app.secret_key = "clave_secreta_productos"


# BASE.HTML - PAGINA PRINCIPAL


@app.route("/")
def index():
    return render_template("base.html")

# EJECUTAR APLICACION

if __name__ == "__main__":
    app.run(debug=True)