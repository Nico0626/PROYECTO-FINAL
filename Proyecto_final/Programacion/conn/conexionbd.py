import mysql.connector
from mysql.connector import Error


class Conexiondb:
    def __init__(self, host, user, password, database):
        """
        Inicializa los parámetros de la conexión a la base de datos.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        """
        Conecta con la base de datos.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            
    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta en la base de datos.
        """
        if self.connection is None:
            print("No hay conexión con la base de datos.")
            return None

        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                # Si la consulta es de tipo SELECT, intentamos consumir todos los resultados
                if query.strip().lower().startswith("select"):
                    resultados = cursor.fetchall()
                    if resultados:
                        print("Resultados obtenidos:")
                        for fila in resultados:
                            print(fila)
                        return resultados
                    else:
                        print("No se encontraron resultados.")
                else:
                    # Para consultas como INSERT, UPDATE, DELETE
                    self.connection.commit()
                    print("Consulta ejecutada exitosamente.")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
    
    
    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")    

conexion = Conexiondb('localhost','root','NM260621','libreria')


conexion.conectar()
conexion.execute_query('SELECT * FROM libros')

conexion.execute_query('''
SELECT v.id_venta, v.fecha_venta, v.total, u.nombre
FROM venta v
JOIN usuario u ON v.id_usuario = u.id_usuario
WHERE v.fecha_venta BETWEEN '2024-01-01' AND '2024-12-31'
''')

conexion.execute_query('''
CREATE TRIGGER actualizar_stock_venta AFTER INSERT ON detalle_venta
FOR EACH ROW
BEGIN
  UPDATE libros
  SET stock = stock - NEW.cantidad
  WHERE id_libro = NEW.id_libro;
END;
''')


conexion.execute_query('''
CREATE TRIGGER restaurar_stock_venta AFTER DELETE ON detalle_venta
FOR EACH ROW
BEGIN
  UPDATE libros
  SET stock = stock + OLD.cantidad
  WHERE id_libro = OLD.id_libro;
END
''')

conexion.execute_query('''
INSERT INTO libros (titulo, autor, precio, stock, fecha_publicacion, genero)
VALUES (%s, %s, %s, %s, %s, %s)
''', ('Nuevo Libro', 'Autor Famoso', 19.99, 10, '2024-01-01', 'Ficción'))

conexion.execute_query('''
UPDATE libros
SET stock = stock + %s
WHERE id_libro = %s
''', (5, 1)) 

conexion.execute_query('''
UPDATE libros
SET stock = 0
WHERE id_libro = %s
''', (1,))

#Consulta de Ventas por Usuario Específico (incluyendo el total de cada venta
conexion.execute_query('''
SELECT v.id_venta, v.fecha_venta, v.total, GROUP_CONCAT(l.titulo SEPARATOR ', ') AS libros_comprados
FROM venta v
JOIN detalle_venta dv ON v.id_venta = dv.id_venta
JOIN libros l ON dv.id_libro = l.id_libro
WHERE v.id_usuario = %s
GROUP BY v.id_venta, v.fecha_venta, v.total
ORDER BY v.fecha_venta DESC
''', (1,))

 def read(self, tabla):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM %s"
            cursor.execute(sql, (tabla))
            row = cursor.fetchone()
            if row:
                return tabla(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()