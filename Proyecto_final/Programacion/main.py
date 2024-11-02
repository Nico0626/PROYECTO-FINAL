from gestor_usuarios import GestorUsuarios
from acceso import Acceso
import time
from colorama import Fore, Style
from usuario import Usuario
import RegistrosPluviales
import captcha

def logo():
    print("logo")

################## login ##################

def login():
    username = input("Usuario: ")
    captcha.resolver_captcha()
    password = input("Contraseña: ")

    # Busca al usuario por nombre de usuario o email
    usuario = Usuario.buscar_usuario(username)

    if usuario and usuario.password == password:
        print("Ingreso exitoso.")
        Acceso.guardar_acceso(Acceso(usuario.username))

        while True:
            logo()
            print("1. Ir a la Gestión de Base de datos")
            print("2. Volver al Menú principal")
            print("3. Cerrar programa")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                menu_base_datos()
            elif opcion == "2":
                print("Cerrando sesión y regresando al menú principal...")
                return  # Salir del login y regresar al menú principal
            elif opcion == "3":
                print("Cerrando programa...")
                exit()
            else:
                print("Opción no válida. Intente de nuevo.")
    else:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Intento fallido: {username}\n")
        print("Credenciales incorrectas.")

################## MENUS ##################

def menu_principal():
    while True:
        logo()
        print("1. Ingresar al sistema con los datos de usuario")
        print("2. Usuarios y Accesos de la Aplicación")
        print("3. Registros pluviales")
        print("4. Cerrar programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            login()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            RegistrosPluviales.main()
            while True:
                print("1. Ingresar otro año")
                print("2. Volver al menú principal")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    RegistrosPluviales()
                elif opcion == "2":
                    menu_principal()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_usuarios():
    while True:
        logo()
        print("\n*** Usuarios y Accesos de la Aplicación ***")
        print("1. Acceder al CRUD de los Usuarios en POO ")
        print("2. Mostrar los datos de Accesos")
        print("3. Ordenamiento y Búsqueda de Usuarios")
        print("4. Volver al Menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud()
        elif opcion == "2":
            accesos()
        elif opcion == "3":
            ordenamiento()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

####################### Acceder al CRUD de los Usuarios en POO ##############

def crud():
    while True:
        logo()
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            GestorUsuarios.agregar_usuario()
        elif opcion == "2":
            GestorUsuarios.modificar_usuario()
        elif opcion == "3":
            GestorUsuarios.eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

############################## Mostrar los datos de Accesos ####################

def accesos():
    while True:
        print("1. Mostrar los Accesos")
        print("2. Mostrar los logs de intentos fallidos")
        print("3. Volver al Menú anterior")
        print("4. Volver al Menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Acceso.guardar_acceso()  # Aquí puede que necesites ajustar según tu implementación
        elif opcion == "2":
            pass  # Implementar función para mostrar logs fallidos
        elif opcion == "3":
            break
        elif opcion == "4":
            menu_principal()
        else:
            print("Opción no válida. Intente de nuevo.")

#######################  Ordenamiento y Búsqueda de Usuarios ########################

def ordenamiento():
    while True:
        logo()
        print("1. Ordenar los Usuarios")
        print("2. Buscar y Mostrar los Usuarios")
        print("3. Volver al Menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            GestorUsuarios.ordenar_usuarios()
        elif opcion == "2":
            mostrar_usuario()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_usuario():
    while True:
        logo()
        print("1. Búsqueda de Usuarios por DNI")
        print("2. Búsqueda de Usuarios por username")
        print("3. Buscar por email")
        print("4. Mostrar todos los usuarios")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pass  # Implementar búsqueda por DNI
        elif opcion == "2":
            pass  # Implementar búsqueda por username
        elif opcion == "3":
            pass  # Implementar búsqueda por email
        elif opcion == "4":
            GestorUsuarios.mostrar_usuarios()
        else:
            print("Opción no válida. Intente de nuevo.")

####################### Menú de Base de Datos ########################

def menu_base_datos():
    while True:
        logo()
        print("\n*** GESTOR BASE DE DATOS ***")
        print("1. Crear base de datos")
        print("2. Crear tablas")
        print("3. Realizar consultas")
        print("4. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pass  # Implementar creación de base de datos
        elif opcion == "2":
            pass  # Implementar creación de tablas
        elif opcion == "3":
            pass  # Implementar realización de consultas
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
