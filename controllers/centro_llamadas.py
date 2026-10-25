from models.excepciones import ColaLlenaError


class CentroLlamadas:
    """Guarda los agentes y la cola de llamadas en espera."""

    def __init__(self, nombre, capacidad_cola):
        self.__nombre = nombre
        self.__agentes = []
        self.__cola_espera = []
        self.__capacidad_cola = capacidad_cola

    def get_nombre(self):
        return self.__nombre

    def get_agentes(self):
        return self.__agentes

    def get_cola_espera(self):
        return self.__cola_espera

    def registrar_agente(self, agente):
        self.__agentes.append(agente)

    def agregar_a_cola(self, llamada):
        # si ya no caben más llamadas, se lanza la excepción
        if len(self.__cola_espera) >= self.__capacidad_cola:
            raise ColaLlenaError(self.__capacidad_cola)
        self.__cola_espera.append(llamada)
        print(f"La llamada {llamada.get_codigo()} quedó en la cola de espera.")

    def buscar_agente_disponible(self, idioma):
        for agente in self.__agentes:
            if agente.esta_disponible() and agente.get_idioma().lower() == idioma.lower():
                return agente
        return None