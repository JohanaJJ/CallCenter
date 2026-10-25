from abc import ABC, abstractmethod


class Agente(ABC):
    """Clase abstracta: lo que tienen en común todos los agentes del call center."""

    def __init__(self, id_agente, nombre, idioma, zona_horaria):
        self.__id_agente = id_agente
        self.__nombre = nombre
        self.__idioma = idioma
        self.__zona_horaria = zona_horaria
        self.__disponible = True

    def get_id_agente(self):
        return self.__id_agente

    def get_nombre(self):
        return self.__nombre

    def get_idioma(self):
        return self.__idioma

    def get_zona_horaria(self):
        return self.__zona_horaria

    def esta_disponible(self):
        return self.__disponible

    def set_nombre(self, nombre):
        if nombre.strip() == "":
            print("Aviso: el nombre está vacío, no se modificó.")
            return False
        self.__nombre = nombre
        return True

    def set_idioma(self, idioma):
        if idioma.strip() == "":
            print("Aviso: el idioma está vacío, no se modificó.")
            return False
        self.__idioma = idioma
        return True

    def set_zona_horaria(self, zona_horaria):
        if zona_horaria.strip() == "":
            print("Aviso: la zona horaria está vacía, no se modificó.")
            return False
        self.__zona_horaria = zona_horaria
        return True

    def set_disponible(self, disponible):
        self.__disponible = disponible

    def mostrar_informacion(self):
        estado = "Disponible" if self.__disponible else "Ocupado"
        print(f"ID: {self.__id_agente}")
        print(f"Nombre: {self.__nombre}")
        print(f"Idioma: {self.__idioma}")
        print(f"Zona horaria: {self.__zona_horaria}")
        print(f"Estado: {estado}")

    @abstractmethod
    def atender_llamada(self):
        """Cada tipo de agente atiende la llamada a su manera."""
        pass

    @abstractmethod
    def calcular_bono(self):
        """Cada tipo de agente calcula su bono con sus propios datos."""
        pass