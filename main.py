from flask import Flask, render_template, request, redirect, flash
from controlador_torneos import ControladorTorneos

app = Flask(__name__)
controlador_torneos = ControladorTorneos()


"""
Definición de rutas
"""


@app.route("/agregar_torneo")
def formulario_agregar_torneo():
    return render_template("agregar_torneo.html")


@app.route("/guardar_torneo", methods=["POST"])
def guardar_torneo():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_torneos.insertar_torneo(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/torneos")


@app.route("/")
@app.route("/torneos")
def torneos():
    torneos = controlador_torneos.obtener_torneos()
    return render_template("torneos.html", torneos=torneos)

@app.route("/mejores")
def mejores():
    return render_template("mejores.html")


@app.route("/eliminar_torneo", methods=["POST"])
def eliminar_torneo():
    controlador_torneos.eliminar_torneo(request.form["id"])
    return redirect("/torneos")


@app.route("/formulario_editar_torneo/<int:id>")
def editar_torneo(id):
    # Obtener el torneo por ID
    torneo = controlador_torneos.obtener_torneo_por_id(id)
    return render_template("editar_torneo.html", torneo=torneo)


@app.route("/actualizar_torneo", methods=["POST"])
def actualizar_torneo():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_torneos.actualizar_torneo(nombre, descripcion, precio, id)
    return redirect("/torneos")


# Iniciar el servidor
if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(host='localhost', port=80, debug=True)