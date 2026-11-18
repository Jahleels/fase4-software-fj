# Fase 4 - Sistema Software FJ

Proyecto colaborativo del curso Programación 213023.

## ¿Qué se debe desarrollar?

Un sistema orientado a objetos en Python para gestionar:

- Clientes.
- Reservas de salas.
- Alquiler de equipos.
- Asesorías especializadas.
- Reservas, confirmaciones y cancelaciones.

El programa no utilizará base de datos. La información se manejará con
objetos y listas; los archivos se usarán únicamente para guardar eventos y
errores.

## Requisitos principales

- Abstracción, herencia, encapsulamiento y polimorfismo.
- Excepciones personalizadas.
- Bloques `try/except`, `else` y `finally`.
- Encadenamiento de excepciones.
- Registro de eventos y errores con `logging`.
- Diez simulaciones válidas e inválidas sin detener el programa.

## Forma de trabajo

Cada integrante debe trabajar en su propia rama, realizar commits claros y
abrir un pull request para integrar sus cambios a `main`.

## Estructura inicial

```text
fase4-software-fj/
├── main.py
├── exceptions/
├── models/
├── utils/
├── tests/
└── logs/
```

Para comprobar la estructura inicial:

```powershell
py main.py
```

La ejecución realiza diez casos válidos e inválidos y guarda los eventos en
`logs/software_fj.log`. Para ejecutar las pruebas:

```powershell
py -m unittest discover -s tests -v
```

## Documentación

- `docs/decisiones_formato.md`: decisiones provisionales y pregunta pendiente.
- `docs/arquitectura.md`: alcance y organización de las clases.
- `docs/casos_simulacion.md`: lista de las diez operaciones.
- `docs/trabajo_colaborativo.md`: propuesta de reparto para el equipo.

Las reglas para ramas, commits y pull requests están en `CONTRIBUTING.md`.

