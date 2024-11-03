from gestor_usuarios import GestorUsuarios
from backend import menu_baseDatos
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
            print("2. Ir al menu principal")
            print("3. Cerrar programa")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                menu_baseDatos()
            elif opcion == "2":
                menu_principal()
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
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al sistema con los datos de usuario")

        print("3. Registros pluviales")
        print("4. Cerrar programa")
        opcion = input("Seleccione una opción: ")

        if opcion=="1":
            menu_usuarios()

        elif opcion == "2":
            login()
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
        print("3. Volver al Menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu()
        elif opcion == "2":
            accesos()

        elif opcion == "3":
            menu_principal()
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
            Acceso.mostrar_accesos()  # Aquí puede que necesites ajustar según tu implementación
        elif opcion == "2":
            pass  # Implementar función para mostrar logs fallidos
        elif opcion == "3":
            break
        elif opcion == "4":
            menu_principal()
        else:
            print("Opción no válida. Intente de nuevo.")

#######################  Ordenamiento y Búsqueda de Usuarios ########################




def menu():
    while True:
        print("\n*** Menú Principal ***")
        logo()
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Buscar usuario")
        print("5. Mostrar todos los usuarios")
        print("6. Ordenar usuarios Burbuja")
        print("7. Ordenar usuarios paython")
        print("8. Ordenar usuarios por dni")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            GestorUsuarios.agregar_usuario()
        elif opcion == "2":
            GestorUsuarios.modificar_usuario()
        elif opcion == "3":
            GestorUsuarios.eliminar_usuario()
        elif opcion == "4":
            user=input("Ingrese el usuario a encontrar: ")
            GestorUsuarios.buscar_usuario(user)
        elif opcion == "5":
            GestorUsuarios.mostrar_usuarios()

        elif opcion == "6":
            GestorUsuarios.ordenar_usuarios_burbuja()

        elif opcion == "7":
            GestorUsuarios.ordenar_usuarios_python()
        
        elif opcion == "8":
            GestorUsuarios.ordenar_usuario_dni()


        elif opcion == "9":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

####################### Menú de Base de Datos ########################



if __name__ == "__main__":
    menu_principal()