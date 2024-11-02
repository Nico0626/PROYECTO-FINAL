from usuario import Usuario
import captcha


class GestorUsuarios:
    usuarios_ordenados = False  # Variable de clase

    @staticmethod
    def agregar_usuario():
        username = input("Ingrese el nombre de usuario: ")
        captcha.resolver_captcha()
        password = input("Ingrese la contraseña: ")
        email = input("Ingrese el correo: ")
        Usuario.crear_usuario(username, password, email)

    @staticmethod
    def modificar_usuario():
        user_id = int(input("Ingrese el ID del usuario a modificar: "))
        username = input("Nuevo username (deje en blanco para no cambiar): ")
        password = input("Nueva contraseña (deje en blanco para no cambiar): ")
        email = input("Nuevo email (deje en blanco para no cambiar): ")
        Usuario.modificar_usuario(user_id, username or None, password or None, email or None)

    @staticmethod
    def eliminar_usuario():
        criterio = input("Ingrese el username o email del usuario a eliminar: ")
        Usuario.eliminar_usuario(criterio)

    @staticmethod
    def mostrar_usuarios():
        usuarios = Usuario.traer_usuarios()
        for usuario in usuarios:
            print(usuario)

    @classmethod
    def ordenar_usuarios_burbuja(cls):
        usuarios = Usuario.traer_usuarios()
        n = len(usuarios)
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios[j].username > usuarios[j + 1].username:
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
        Usuario.guardar_usuarios(usuarios)
        cls.usuarios_ordenados = True  # Actualiza la variable de clase
        print("Usuarios ordenados por burbuja y guardados en usuarios.ispc.")

    @classmethod
    def ordenar_usuarios_python(cls):
        usuarios = Usuario.traer_usuarios()
        usuarios.sort(key=lambda usuario: usuario.username)
        Usuario.guardar_usuarios(usuarios)
        cls.usuarios_ordenados = True  # Actualiza la variable de clase
        print("Usuarios ordenados usando sort() de Python y guardados en usuarios.ispc.")

    @classmethod
    def buscar_usuario(cls, username):
        usuarios = Usuario.traer_usuarios()
        if cls.usuarios_ordenados:
            print("Búsqueda realizada usando búsqueda binaria.")
            return cls.busqueda_binaria(usuarios, username)
        else:
            print("Búsqueda realizada usando búsqueda secuencial.")
            return cls.busqueda_secuencial(usuarios, username)

    @staticmethod
    def busqueda_secuencial(usuarios, username):
        for usuario in usuarios:
            if usuario.username == username: 
                print(usuario)
            else:
                print("Usuario no encontrado")

    @staticmethod
    def busqueda_binaria(usuarios, username):
        izquierda, derecha = 0, len(usuarios) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if usuarios[medio].username == username:
                print("usuarios")[medio]
            elif usuarios[medio].username < username:
                izquierda = medio + 1
            else:
                derecha = medio - 1
                print("Usuario no encontrado")