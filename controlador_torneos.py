from bd import obtener_conexion


class ControladorTorneos:
    def insertar_torneo(self, nombre, descripcion, precio):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO torneos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
                           (nombre, descripcion, precio))
        conexion.commit()
        conexion.close()

    def obtener_torneos(self):
        conexion = obtener_conexion()
        torneos = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio FROM torneos")
            torneos = cursor.fetchall()
        conexion.close()
        return torneos

    def eliminar_torneo(self, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM torneos WHERE id = %s", (id,))
        conexion.commit()
        conexion.close()

    def obtener_torneo_por_id(self, id):
        conexion = obtener_conexion()
        torneo = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT id, nombre, descripcion, precio FROM torneos WHERE id = %s", (id,))
            torneo = cursor.fetchone()
        conexion.close()
        return torneo

    def actualizar_torneo(self, nombre, descripcion, precio, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE torneos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                           (nombre, descripcion, precio, id))
        conexion.commit()
        conexion.close()
