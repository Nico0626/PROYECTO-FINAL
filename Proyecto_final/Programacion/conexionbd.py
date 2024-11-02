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
        
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Consulta ejecutada exitosamente.")
            return cursor.fetchall()  # Retorna los resultados si hay
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            cursor.close()
    
    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")    

conexion = Conexiondb('localhost','root','valeria11','libreria')

conexion.conectar()

if conexion.connection is None:
    print("Error al conectar a la base de datos.")
else:
    print("Conexión establecida correctamente.")
