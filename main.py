from models.agente import Agente
from models.agente_soporte import AgenteSoporte
from models.agente_ventas import AgenteVentas
from models.agente_cobranza import AgenteCobranza
from models.cliente import Cliente
from models.llamada import Llamada
from models.excepciones import (
    AgenteNoDisponibleError,
    IdiomaNoSoportadoError,
    ColaLlenaError,
)
from controllers.centro_llamadas import CentroLlamadas

# Agente es abstracta, no se puede crear
print("--- Intentando crear un Agente genérico ---")
try:
    agente_generico = Agente("AG0000", "Agente Prueba", "Español", "UTC-5")
except TypeError as error:
    print("Se controló el error:", error)

# Centro de llamadas y agentes
centro = CentroLlamadas("Call Center Bogotá", 2)

soporte1 = AgenteSoporte("AG4821", "Camila Ríos", "Español", "UTC-5", 2)
soporte2 = AgenteSoporte("AG7305", "Daniel Ortiz", "Inglés", "UTC-5", 1)
ventas1 = AgenteVentas("AG1927", "Laura Gómez", "Español", "UTC-5", 3)
ventas2 = AgenteVentas("AG5063", "Mateo Rojas", "Inglés", "UTC-3", 2)
cobranza1 = AgenteCobranza("AG8142", "Juliana Pardo", "Español", "UTC-5", 5)

for agente in (soporte1, soporte2, ventas1, ventas2, cobranza1):
    centro.registrar_agente(agente)

# Clientes
cliente1 = Cliente("1032456789", "Sofía Herrera", "México", "Español", "+52 55 4821 7305")
cliente2 = Cliente("P4829175", "John Miller", "Estados Unidos", "Inglés", "+1 305 555 0142")
cliente3 = Cliente("80194532", "Andrés Castaño", "Colombia", "Español", "+57 310 482 1957")
cliente4 = Cliente("FR7305182", "Marie Dupont", "Francia", "Francés", "+33 6 12 34 56 78")

# Llamadas
llamada1 = Llamada("L1001", cliente1, "Falla en el servicio de internet")
llamada2 = Llamada("L1002", cliente2, "Oferta de un nuevo plan")
llamada3 = Llamada("L1003", cliente3, "Pago pendiente de la factura")
llamada4 = Llamada("L1004", cliente1, "Consulta sobre un plan nuevo")
llamada5 = Llamada("L1005", cliente3, "Cambio de plan")
llamada6 = Llamada("L1006", cliente4, "Problema con la facturación")
llamada7 = Llamada("L1007", cliente2, "Reclamo por cobro")

# Casos normales
print("\n--- Llamada de soporte ---")
llamada1.asignar_agente(soporte1)
soporte1.atender_llamada()
soporte1.registrar_ticket()
llamada1.finalizar_llamada(12, "Problema resuelto")
llamada1.mostrar_llamada()

print("\n--- Llamada de ventas ---")
llamada2.asignar_agente(ventas2)
ventas2.atender_llamada()
ventas2.registrar_venta()
llamada2.finalizar_llamada(8, "Venta cerrada")
llamada2.mostrar_llamada()

print("\n--- Llamada de cobranza ---")
llamada3.asignar_agente(cobranza1)
cobranza1.atender_llamada()
cobranza1.registrar_pago(350000)
llamada3.finalizar_llamada(15, "Pago acordado")
llamada3.mostrar_llamada()

# Excepciones
print("\n--- Agente ocupado ---")
llamada4.asignar_agente(ventas1)
try:
    llamada5.asignar_agente(ventas1)
except AgenteNoDisponibleError as error:
    print("Se controló el error:", error)
    centro.agregar_a_cola(llamada5)

print("\n--- Idioma que el agente no habla ---")
try:
    llamada6.asignar_agente(soporte1)
except IdiomaNoSoportadoError as error:
    print("Se controló el error:", error)
    centro.agregar_a_cola(llamada6)

print("\n--- Buscando un agente que hable francés ---")
agente_frances = centro.buscar_agente_disponible("Francés")
if agente_frances is None:
    print("No hay ningún agente disponible que hable francés.")

print("\n--- Cola de espera llena ---")
try:
    centro.agregar_a_cola(llamada7)
except ColaLlenaError as error:
    print("Se controló el error:", error)

print("\nEl programa siguió funcionando después de cada error.")

# Polimorfismo: una sola lista con los tres tipos de agente
print("\n--- Todos los agentes ---")
agentes = [soporte1, ventas1, cobranza1, soporte2, ventas2]

for agente in agentes:
    agente.mostrar_informacion()
    agente.atender_llamada()
    print(f"Bono: ${agente.calcular_bono():,.0f}")
    print("-" * 40)