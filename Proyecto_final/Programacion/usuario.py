import os
import pickle

class Usuario:
    next_id = 1

    def __init__(self, username, password, email, dni):
        self._id = Usuario.next_id
        self._username = username
        self._password = password
        self._email = email
        self._dni = dni
        Usuario.next_id += 1

    def __repr__(self):
        return f"Usuario: {self._id}, Username: {self._username}, Email: {self._email}, Dni: {self._dni}"

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def dni(self):    
        return self._dni
    
    @dni.setter
    def dni(self, value):  
        if len(value)!=8 or not value.isdigit():
            raise ValueError("DNI inválido. Debe tener 8 dígitos.")
        self._dni = value

    @classmethod
    def traer_usuarios(cls):
        if os.path.exists('usuarios.ispc'):
            try:
                with open('usuarios.ispc', 'rb') as file:
                    return pickle.load(file)
            except (EOFError, pickle.PickleError):
                return []
        return []

    @classmethod
    def guardar_usuarios(cls, usuarios):
        with open('usuarios.ispc', 'wb') as file:
            pickle.dump(usuarios, file)

    @classmethod
    def crear_usuario(cls, username, password, email, dni):
        usuarios = cls.traer_usuarios()
        if any(u.username == username or u.email == email for u in usuarios):
            print("Error: El nombre de usuario o el correo ya están en uso.")
            return
        
        nuevo_usuario = cls(username, password, email, dni)
        usuarios.append(nuevo_usuario)
        cls.guardar_usuarios(usuarios)
        print(f"Usuario {username} creado exitosamente.")

    @classmethod
    def modificar_usuario(cls, user_id, username=None, password=None, email=None, dni=None):
        usuarios = cls.traer_usuarios()
        for usuario in usuarios:
            if usuario.id == user_id:
                if username:
                    usuario.username = username
                if password:
                    usuario.password = password
                if email:
                    usuario.email = email
                if dni:
                    usuario.dni = dni
                cls.guardar_usuarios(usuarios)
                print(f"Usuario con ID {user_id} actualizado.")
                return True
        print(f"Usuario con ID {user_id} no encontrado.")
        return False

    @classmethod
    def eliminar_usuario(cls, criterio):
        usuarios = cls.traer_usuarios()
        usuarios_filtrados = [usuario for usuario in usuarios if usuario.username != criterio and usuario.email != criterio]
        if len(usuarios) == len(usuarios_filtrados):
            print("No se encontró ningún usuario con ese criterio.")
        else:
            cls.guardar_usuarios(usuarios_filtrados)
            print("Usuario eliminado con éxito.")

    @classmethod
    def buscar_usuario(cls, criterio):
        usuarios = cls.traer_usuarios()
        for usuario in usuarios:
            if cls.username == criterio or cls.email == criterio:
                return usuario
        print("Usuario no encontrado.")
        return None
