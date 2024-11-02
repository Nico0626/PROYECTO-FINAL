import os
import pickle
import time

class Acceso:
    def __init__(self, usuario_logueado):
        self.fecha_ingreso = time.strftime("%Y-%m-%d %H:%M:%S")
        self.usuario_logueado = usuario_logueado

    @classmethod
    def guardar_acceso(cls, acceso):
        accesos = cls.traer_accesos()
        accesos.append(acceso)
        with open('accesos.ispc', 'wb') as file:
            pickle.dump(accesos, file)

    @classmethod
    def traer_accesos(cls):
        if os.path.exists('accesos.ispc'):
            with open('accesos.ispc', 'rb') as file:
                return pickle.load(file)
        return []
    @classmethod
    def mostrar_accesos(cls):
        accesos = cls.traer_accesos()
        for acceso in accesos:
            print(acceso)