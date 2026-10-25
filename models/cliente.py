class Cliente:
    """Persona que llama al call center."""

    def __init__(self, id_cliente, nombre, pais, idioma, telefono):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__pais = pais
        self.__idioma = idioma
        self.__telefono = telefono

    def get_id_cliente(self):
        return self.__id_cliente

    def get_nombre(self):
        return self.__nombre

    def get_pais(self):
        return self.__pais

    def get_idioma(self):
        return self.__idioma

    def get_telefono(self):
        return self.__telefono

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

    def set_telefono(self, telefono):
        if telefono.strip() == "":
            print("Aviso: el teléfono está vacío, no se modificó.")
            return False
        self.__telefono = telefono
        return True

    def mostrar_informacion(self):
        print(f"ID cliente: {self.__id_cliente}")
        print(f"Nombre: {self.__nombre}")
        print(f"País: {self.__pais}")
        print(f"Idioma: {self.__idioma}")
        print(f"Teléfono: {self.__telefono}")