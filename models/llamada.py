from models.registro_llamada import RegistroLlamada
from models.excepciones import AgenteNoDisponibleError, IdiomaNoSoportadoError


class Llamada:
    """Llamada de un cliente. Crea su propio registro y recibe un agente."""

    def __init__(self, codigo, cliente, motivo):
        self.__codigo = codigo
        self.__cliente = cliente            # objeto Cliente ya creado
        self.__motivo = motivo
        self.__estado = "En espera"
        self.__agente = None                # se asigna después
        # la llamada crea su propio registro (composición)
        self.__registro = RegistroLlamada()

    def get_codigo(self):
        return self.__codigo

    def get_cliente(self):
        return self.__cliente

    def get_agente(self):
        return self.__agente

    def get_estado(self):
        return self.__estado

    def get_registro(self):
        return self.__registro

    def asignar_agente(self, agente):
        # primero se revisa que el agente esté libre
        if not agente.esta_disponible():
            raise AgenteNoDisponibleError(agente.get_nombre())
        # luego que hable el idioma del cliente
        if agente.get_idioma().lower() != self.__cliente.get_idioma().lower():
            raise IdiomaNoSoportadoError(agente.get_nombre(), agente.get_idioma(),
                                         self.__cliente.get_idioma())
        self.__agente = agente
        agente.set_disponible(False)
        self.__estado = "En curso"
        print(f"La llamada {self.__codigo} fue asignada a {agente.get_nombre()}.")

    def finalizar_llamada(self, duracion, resultado):
        if self.__agente is None:
            print("No se puede finalizar una llamada que no tiene agente.")
            return False
        if self.__registro.registrar_cierre(duracion, resultado):
            self.__estado = "Finalizada"
            self.__agente.set_disponible(True)
            return True
        return False

    def mostrar_llamada(self):
        print(f"Llamada {self.__codigo} - Estado: {self.__estado}")
        print(f"Cliente: {self.__cliente.get_nombre()} ({self.__cliente.get_pais()})")
        print(f"Motivo: {self.__motivo}")
        if self.__agente is not None:
            print(f"Agente: {self.__agente.get_nombre()}")
        else:
            print("Agente: sin asignar")
        self.__registro.mostrar_registro()