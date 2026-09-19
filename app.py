# ==========================================================
# IMPORTACIONES
# ==========================================================

from flask import Flask, render_template
from psycopg2.extras import RealDictCursor
from db import get_connection


# ==========================================================
# CONFIGURACION GENERAL
# ==========================================================

app = Flask(__name__)

# Clave necesaria para utilizar mensajes flash más adelante
app.secret_key = "clave_secreta_productos"


# ==========================================================
# BASE.HTML - PAGINA BASE
# ==========================================================

@app.route("/base")
def base():

    # Mostrar la plantilla base.html
    return render_template("base.html")


# ==========================================================
# INDEX.HTML - LISTAR PRODUCTOS
# ==========================================================

@app.route("/")
def index():

    # Abrir conexión a PostgreSQL
    conexion = get_connection()

    # Crear cursor como diccionario
    # Esto permite usar:
    # producto.nombre
    # producto.precio
    # producto.stock
    cursor = conexion.cursor(
        cursor_factory=RealDictCursor
    )

    # Consultar todos los productos registrados
    cursor.execute("""
        SELECT id,
               nombre,
               codigo,
               precio,
               stock,
               categoria,
               activo,
               fecha_registro
        FROM productos
        ORDER BY id DESC
    """)

    # Obtener todos los productos encontrados
    productos = cursor.fetchall()

    # Cerrar cursor
    cursor.close()

    # Cerrar conexión
    conexion.close()

    # Enviar la lista de productos a index.html
    return render_template(
        "index.html",
        productos=productos
    )


# ==========================================================
# EJECUTAR APLICACION
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)