# Call Center Internacional

Proyecto final: sistema de información hecho con Programación Orientada a Objetos en Python.

## Integrantes

- Johana Jiménez

## Descripción general

El sistema simula un call center internacional. Los clientes llaman desde distintos países,
y cada llamada se asigna a un agente que esté disponible y hable el idioma del cliente.
Cuando la llamada termina se guarda cómo salió. Además, el sistema controla los problemas
que pueden pasar: que el agente esté ocupado, que no hable el idioma o que la cola de espera
esté llena.

## Estructura de los archivos

- `main.py`: programa principal con las pruebas.
- `models/`: las clases del sistema (`agente.py`, `agente_soporte.py`, `agente_ventas.py`,
  `agente_cobranza.py`, `cliente.py`, `llamada.py`, `registro_llamada.py` y `excepciones.py`).
- `controllers/centro_llamadas.py`: guarda los agentes y la cola de espera.
- `Diagramas/`: diagrama UML de clases hecho en draw.io.
- `Documentos/`: documento de decisiones de diseño.

## Cómo ejecutarlo

Con Python instalado, en la carpeta del proyecto se escribe:

```
py main.py
```

## Clases, herencia y clase abstracta

`Agente` es una clase abstracta: tiene lo que todos los agentes tienen en común (id, nombre,
idioma, zona horaria y si está disponible). No se pueden crear agentes genéricos porque cada
agente es de un tipo. Sus métodos `atender_llamada()` y `calcular_bono()` son abstractos.

Tres clases heredan de `Agente`: `AgenteSoporte`, `AgenteVentas` y `AgenteCobranza`. Un agente
de soporte, de ventas o de cobranza **es un** agente, y cada uno agrega sus propios datos
(tickets, ventas o monto recuperado).

Las demás clases son `Cliente`, `Llamada`, `RegistroLlamada` y `CentroLlamadas`.

## Sobrescritura y polimorfismo

Las tres clases hijas sobrescriben `atender_llamada()`, `calcular_bono()` y
`mostrar_informacion()`. El nombre es el mismo, pero el resultado cambia según el tipo de agente
y usa sus datos propios.

En `main.py` hay una sola lista con agentes de los tres tipos y se recorre con un único
`for`, llamando siempre a los mismos métodos, sin usar `if` para preguntar el tipo.

## Composición

`Llamada` crea su propio `RegistroLlamada` dentro del constructor. Usé composición porque el
registro (duración y resultado) solo tiene sentido como parte de una llamada y no existe por
su cuenta: una llamada **tiene un** registro. No usé herencia porque un registro no es un tipo
de llamada ni una llamada es un tipo de registro.

## Otras relaciones entre objetos

- `Llamada` se relaciona con un `Cliente` y con un `Agente` que ya existen.
- `CentroLlamadas` guarda una lista de agentes y una cola de llamadas en espera.

## Excepciones personalizadas

Están en `models/excepciones.py` y heredan de `CallCenterError`:

- `AgenteNoDisponibleError`: se lanza en `Llamada.asignar_agente()` si el agente está ocupado.
- `IdiomaNoSoportadoError`: se lanza en `Llamada.asignar_agente()` si el agente no habla el
  idioma del cliente.
- `ColaLlenaError`: se lanza en `CentroLlamadas.agregar_a_cola()` si ya no caben más llamadas.

Las tres se capturan en `main.py` y el programa sigue funcionando.

## Uso de herramientas de inteligencia artificial

Usé Claude (una herramienta de IA) como apoyo para plantear el tema y las clases, armar el
diagrama y el código base y resolver errores de Git. Revisé el código, lo probé y cambié datos
y mensajes. El detalle está en el Documento de Decisiones de Diseño.