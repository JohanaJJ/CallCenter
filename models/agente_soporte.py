from models.agente import Agente


class AgenteSoporte(Agente):
    """Agente que resuelve problemas técnicos de los clientes."""

    def __init__(self, id_agente, nombre, idioma, zona_horaria, nivel_soporte):
        super().__init__(id_agente, nombre, idioma, zona_horaria)
        self.__nivel_soporte = nivel_soporte
        self.__tickets_resueltos = 0

    def get_nivel_soporte(self):
        return self.__nivel_soporte

    def get_tickets_resueltos(self):
        return self.__tickets_resueltos

    def set_nivel_soporte(self, nivel_soporte):
        if nivel_soporte <= 0:
            print("No se pudo cambiar el nivel: debe ser mayor que cero.")
            return False
        self.__nivel_soporte = nivel_soporte
        return True

    def registrar_ticket(self):
        self.__tickets_resueltos += 1

    def atender_llamada(self):
        print(f"{self.get_nombre()} (soporte nivel {self.__nivel_soporte}) "
              f"revisa el problema del cliente y busca una solución.")

    def calcular_bono(self):
        return self.__tickets_resueltos * 5000

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Agente de soporte")
        print(f"Nivel de soporte: {self.__nivel_soporte}")
        print(f"Tickets resueltos: {self.__tickets_resueltos}")