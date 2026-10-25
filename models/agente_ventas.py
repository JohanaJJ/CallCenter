from models.agente import Agente


class AgenteVentas(Agente):
    """Agente que ofrece productos y servicios a los clientes."""

    def __init__(self, id_agente, nombre, idioma, zona_horaria, meta_mensual):
        super().__init__(id_agente, nombre, idioma, zona_horaria)
        self.__meta_mensual = meta_mensual
        self.__ventas_cerradas = 0

    def get_meta_mensual(self):
        return self.__meta_mensual

    def get_ventas_cerradas(self):
        return self.__ventas_cerradas

    def set_meta_mensual(self, meta_mensual):
        if meta_mensual <= 0:
            print("No se pudo cambiar la meta: debe ser mayor que cero.")
            return False
        self.__meta_mensual = meta_mensual
        return True

    def registrar_venta(self):
        self.__ventas_cerradas += 1

    def atender_llamada(self):
        print(f"{self.get_nombre()} (ventas) presenta una oferta al cliente "
              f"y le explica los beneficios.")

    def calcular_bono(self):
        bono = self.__ventas_cerradas * 20000
        if self.__ventas_cerradas >= self.__meta_mensual:
            bono += 100000
        return bono

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Agente de ventas")
        print(f"Meta mensual: {self.__meta_mensual}")
        print(f"Ventas cerradas: {self.__ventas_cerradas}")