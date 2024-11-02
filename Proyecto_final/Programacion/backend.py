import mysql.connector
from mysql.connector import Error

class Conexiondb:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa")
                return True
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            return False

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("No hay conexión con la base de datos.")
            return None

        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if query.strip().lower().startswith("select"):
                resultados = cursor.fetchall()
                cursor.close()
                if resultados:
                    print("Resultados obtenidos:")
                    for fila in resultados:
                        print(fila)
                    return resultados
                else:
                    print("No se encontraron resultados.")
            else:
                self.connection.commit()
                cursor.close()
                print("Consulta ejecutada exitosamente.")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

conexion = Conexiondb('localhost', 'root', 'contraseña', 'libreria')

def menu_baseDatos():
    while True:
        print("\nMenu de Base de Datos:")
        print("1. Ver tablas disponibles.")
        print("2. Insertar un nuevo registro.")
        print("3. Actualizar un registro.")
        print("4. Eliminar un registro.")
        print("5. Consultar registros de una tabla.")
        print("6. Salir.")
        
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            mostrar_tablas()
        elif opcion == 2:
            insertar_registro()
        elif opcion == 3:
            actualizar_registro()
        elif opcion == 4:
            eliminar_registro()
        elif opcion == 5:
            consultar_todos_registros()
        elif opcion == 6:
            print("Saliendo del menú de base de datos.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_tablas():
    conexion.conectar()
    query = "SHOW TABLES"
    tablas = conexion.execute_query(query)
    if tablas:
        print("Tablas disponibles:")
        for tabla in tablas:
            print(tabla['Tables_in_libreria'])
    conexion.close()

def consultar_todos_registros():
    conexion.conectar()
    tabla = input("Ingrese el nombre de la tabla a consultar: ")
    query = f"SELECT * FROM {tabla}"
    conexion.execute_query(query)
    conexion.close()
    
def insertar_registro():
    conexion.conectar()
    print("Tablas disponibles para inserción: usuario, libros, venta, detalle_venta")
    tabla = input("Seleccione la tabla para insertar un registro: ").strip().lower()

    if tabla == "usuario":
        nombre = input("Ingrese el nombre: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el teléfono (opcional): ")
        query = "INSERT INTO usuario (nombre, email, telefono) VALUES (%s, %s, %s)"
        conexion.execute_query(query, (nombre, email, telefono if telefono else None))

    elif tabla == "libros":
        titulo = input("Ingrese el título: ")
        autor = input("Ingrese el autor: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))
        fecha_publicacion = input("Ingrese la fecha de publicación (YYYY-MM-DD): ")
        genero = input("Ingrese el género: ")
        query = "INSERT INTO libros (titulo, autor, precio, stock, fecha_publicacion, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        conexion.execute_query(query, (titulo, autor, precio, stock, fecha_publicacion, genero))
        conexion.close()

    elif tabla == "venta":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        total = float(input("Ingrese el total de la venta: "))
        query = "INSERT INTO venta (id_usuario, total) VALUES (%s, %s)"
        conexion.execute_query(query, (id_usuario, total))
        conexion.close()


    elif tabla == "detalle_venta":
        id_venta = int(input("Ingrese el ID de la venta: "))
        id_libro = int(input("Ingrese el ID del libro: "))
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))
        query = "INSERT INTO detalle_venta (id_venta, id_libro, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)"
        conexion.execute_query(query, (id_venta, id_libro, cantidad, precio_unitario))
        conexion.close()

    else:
        print("Tabla no válida.")
    
    conexion.close()

def actualizar_registro():
    conexion.conectar()
    print("Tablas disponibles para actualización: usuario, libros")
    tabla = input("Seleccione la tabla para actualizar un registro: ").strip().lower()

    if tabla == "usuario":
        id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_email = input("Ingrese el nuevo email: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono (opcional): ")
        query = "UPDATE usuario SET nombre = %s, email = %s, telefono = %s WHERE id_usuario = %s"
        conexion.execute_query(query, (nuevo_nombre, nuevo_email, nuevo_telefono if nuevo_telefono else None, id_usuario))

    elif tabla == "libros":
        id_libro = int(input("Ingrese el ID del libro a actualizar: "))
        nuevo_titulo = input("Ingrese el nuevo título: ")
        nuevo_autor = input("Ingrese el nuevo autor: ")
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        query = "UPDATE libros SET titulo = %s, autor = %s, precio = %s, stock = %s WHERE id_libro = %s"
        conexion.execute_query(query, (nuevo_titulo, nuevo_autor, nuevo_precio, nuevo_stock, id_libro))

    else:
        print("Tabla no válida o función incompleta.")
    
    conexion.close()

def eliminar_registro():
    conexion.conectar()
    print("Tablas disponibles para eliminación: usuario, libros")
    tabla = input("Seleccione la tabla para eliminar un registro: ").strip().lower()

    if tabla == "usuario":
        id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
        query = "DELETE FROM usuario WHERE id_usuario = %s"
        conexion.execute_query(query, (id_usuario,))

    elif tabla == "libros":
        id_libro = int(input("Ingrese el ID del libro a eliminar: "))
        query = "DELETE FROM libros WHERE id_libro = %s"
        conexion.execute_query(query, (id_libro,))

    else:
        print("Tabla no válida o función incompleta.")
    
    conexion.close()


