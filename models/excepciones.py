class CallCenterError(Exception):
    """Error base del sistema del call center."""
    pass


class AgenteNoDisponibleError(CallCenterError):
    def __init__(self, nombre_agente):
        super().__init__(f"El agente {nombre_agente} no está disponible en este momento.")


class IdiomaNoSoportadoError(CallCenterError):
    def __init__(self, nombre_agente, idioma_agente, idioma_cliente):
        super().__init__(
            f"{nombre_agente} habla {idioma_agente}, pero el cliente necesita {idioma_cliente}.")


class ColaLlenaError(CallCenterError):
    def __init__(self, capacidad):
        super().__init__(f"La cola de espera está llena (máximo {capacidad} llamadas).")