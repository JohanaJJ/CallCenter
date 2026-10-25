class RegistroLlamada:
    """Guarda cómo terminó una llamada. Lo crea la propia Llamada."""

    def __init__(self):
        self.__duracion_minutos = 0
        self.__resultado = "Sin resultado"
        self.__observaciones = ""

    def get_duracion_minutos(self):
        return self.__duracion_minutos

    def get_resultado(self):
        return self.__resultado

    def get_observaciones(self):
        return self.__observaciones

    def set_observaciones(self, texto):
        self.__observaciones = texto

    def registrar_cierre(self, duracion, resultado):
        if duracion <= 0:
            print("No se pudo registrar el cierre: la duración debe ser mayor que cero.")
            return False
        self.__duracion_minutos = duracion
        self.__resultado = resultado
        return True

    def mostrar_registro(self):
        print(f"Duración: {self.__duracion_minutos} minutos")
        print(f"Resultado: {self.__resultado}")
        if self.__observaciones != "":
            print(f"Observaciones: {self.__observaciones}")