from models.agente import Agente


class AgenteCobranza(Agente):
    """Agente que contacta clientes para recordarles pagos pendientes."""

    def __init__(self, id_agente, nombre, idioma, zona_horaria, porcentaje_comision):
        super().__init__(id_agente, nombre, idioma, zona_horaria)
        self.__monto_recuperado = 0
        self.__porcentaje_comision = porcentaje_comision

    def get_monto_recuperado(self):
        return self.__monto_recuperado

    def get_porcentaje_comision(self):
        return self.__porcentaje_comision

    def set_porcentaje_comision(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("No se pudo cambiar la comisión: debe estar entre 0 y 100.")
            return False
        self.__porcentaje_comision = porcentaje
        return True

    def registrar_pago(self, monto):
        if monto <= 0:
            print("No se pudo registrar el pago: el monto debe ser mayor que cero.")
            return
        self.__monto_recuperado += monto

    def atender_llamada(self):
        print(f"{self.get_nombre()} (cobranza) le recuerda al cliente "
              f"su pago pendiente y acuerda una fecha.")

    def calcular_bono(self):
        return self.__monto_recuperado * self.__porcentaje_comision / 100

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Agente de cobranza")
        print(f"Monto recuperado: {self.__monto_recuperado}")
        print(f"Comisión: {self.__porcentaje_comision}%")