# Sistema de Gestión de Países

## Descripción del Proyecto

Sistema de Gestión de Países desarrollado en Python que trabaja sobre el archivo `paises.csv`. El programa permite:

- Mostrar todos los países cargados.
- Agregar un nuevo país.
- Actualizar la información de un país existente.
- Buscar un país por nombre.
- Filtrar países por campo (continente, población, superficie).
- Ordenar países por un campo determinado, de forma ascendente o descendente.
- Guardar los cambios realizados en el archivo `.csv`.
- Salir del programa.

La arquitectura del proyecto está consolidada en un único archivo `main.py`, diseñado de forma modular, con funciones de responsabilidad única y sin uso de variables globales.

## Datos de la Universidad y la Cátedra

- **Universidad:** Universidad Tecnológica Nacional (UTN) — Modalidad a Distancia
- **Cátedra:** Programación 1
- **Coordinador:** Alberto Cortez
- **Año:** 2026

## Profesores

- Ariel Enferrel
- Martín A. García
- Cinthia Rigoni

## Tutores

- Virginia Cimino
- Luciano Chiroli

## Integrantes

- Nehuel Mendoza - Comisión 27
- Santiago Luis Diaz - Comision 7


## Estructura del Proyecto

```
TPI-Programacion-1-UTN-a-distancia/
├── main.py        # Lógica principal del sistema: menú, CRUD, filtros, orden y estadísticas
├── paises.csv      # Archivo de datos con la información de los países
└── README.md       # Este archivo
```

## Instrucciones de Ejecución

1. **Clonar el repositorio** (opción recomendada):
   ```bash
   git clone https://github.com/santiago-diaz-code/TPI-Programacion-1-UTN-a-distancia.git
   ```
   O bien, **descargar el proyecto como .zip** desde GitHub: botón verde **"Code"** → **"Download ZIP"**, y descomprimir la carpeta.

2. **Abrir la carpeta del proyecto en Visual Studio Code** (`File → Open Folder`).

3. **Verificar que Python esté instalado** (versión 3.x). Se puede comprobar con:
   ```bash
   python --version
   ```

4. **Ejecutar el programa** desde una terminal integrada de VS Code (`Terminal → New Terminal`):
   ```bash
   python main.py
   ```

5. **Utilizar el menú interactivo** que se muestra en consola para navegar entre las distintas opciones (mostrar, agregar, actualizar, buscar, filtrar, ordenar, guardar y salir).

## Uso de Librerías de Terceros

El proyecto utiliza únicamente módulos de la librería estándar de Python, por lo que no requiere instalación de dependencias externas (`pip install`):


## Links

- [**Repositorio de GitHub**](https://github.com/santiago-diaz-code/TPI-Programacion-1-UTN-a-distancia/)
- [**Video explicativo**](https://youtu.be/Ou9Drw80sFQ)
- [**Documentación**](https://drive.google.com/file/d/1_DV2SyQHnwWahPoYS754GDAp33Cwihjw/view?usp=sharing)

## Ejemplos de Entrada y Salida

**Ejemplo 1 — Mostrar todos los países**

```
=== SISTEMA DE GESTIÓN DE PAÍSES ===
1. Mostrar todos los países
2. Agregar país
3. Actualizar país
4. Buscar país
5. Filtrar por campo
6. Ordenar por campo
7. Guardar cambios
8. Salir
Seleccione una opción: 1

Nombre        Continente     Población      Superficie (km²)
Argentina     América        45.000.000     2.780.400
Brasil        América        214.000.000    8.515.770
Japón         Asia           125.000.000    377.975
```

**Ejemplo 2 — Agregar un nuevo país**

```
Seleccione una opción: 2
Ingrese el nombre del país: Uruguay
Ingrese el continente: América
Ingrese la población: 3.500.000
Ingrese la superficie (km²): 176.215

País agregado correctamente.
```

**Ejemplo 3 — Filtrar por continente**

```
Seleccione una opción: 5
Ingrese el campo a filtrar (continente/población/superficie): continente
Ingrese el valor: América

Nombre        Continente     Población      Superficie (km²)
Argentina     América        45.000.000     2.780.400
Brasil        América        214.000.000    8.515.770
Uruguay       América        3.500.000      176.215
```



