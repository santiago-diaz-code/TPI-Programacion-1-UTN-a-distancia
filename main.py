import csv
import os
#---Módulo de Validaciones---
#------FUNCIÓN: Solicitar entero positivo------
def solicitar_entero_positivo(mensaje):
    while True: #Bucle infinito de control: solo se rompe con un ingreso inválido.
        try:
            #Captura la entrada de texto e intenta convertirla a tipo int.
            valor = int(input(mensaje))
            if valor > 0:
                return valor #Retorna el valor validado y corta la ejecución del bucle.
            print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            #Captura el error en caso de que el usuario ingrese caracteres no numéricos.
            print("Entrada no válida. Por favor, ingrese un número entero.")

#------FUNCIÓN: Solicitar texto (obligatorio)------
def solicitar_texto(mensaje): #Esto para evitar que el usuario deje espacios vacíos.
    while True:
        #Lee la entrada y quita los espacios que se encuentren vacíos tanto al principio como al final.
        valor = input(mensaje).strip()
        if valor:
            return valor #Retorna el texto limpio de espacios.
        print("Este campo es obligatorio. Por favor, ingrese un valor.")

#---Módulo de Funciones Operativas
#------FUNCIÓN: Cargar países desde el archivo CSV------
def cargar_paises(ruta_archivo="paises.csv"): #Esta función lee el archivo CSV y carga los países en la lista.
    lista_paises = [] #Lista dinámica que funcionará como contenedor de registros.
    #Control de existencias: para evitar un error fatal (FileNotFoundError) en el sistema.
    if not os.path.exists(ruta_archivo):
        print(f"El archivo {ruta_archivo} no existe. Se iniciará con una lista vacía.")
        return lista_paises

    try:
        #Apertura del archivo usando 'with' para garantizar su cierre automático. Se abre el archivo en modo lectura.
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            #Lee automáticamente la primera fila del archivo CSV y los guarda internamente.
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv: #Inicia una iteración línea por línea sobre el set de datos. 
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais) #Una vez estructurado y validado el diccionario local con los tipos de datos correctos, se agrega el nuevo país con sus demás elementos al final de lista_paises.
                except (ValueError, KeyError): #Validación para que no hayan campos vacíos o con formato distinto al solicitado. KeyError se mostrará en caso de que en una fila se haya omitido completar las columnas correspondientes.
                    continue
        print("Datos cargados correctamente desde el archivo CSV.")
    #Captura problemas de infraestructura del sistema, como puede ser que el archivo esté bloqueado por otro programa que tiene permisos de administrador.
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return lista_paises

#------FUNCIÓN: Guardar países en el archivo CSV------
def guardar_paises(lista_paises, ruta_archivo="paises.csv"): #Esta función guarda la lista de países en el archivo CSV.
    try:
        #El modo write sobreescribe el archivo con la información actualizada de la sesión.
        with open(ruta_archivo, mode='w', encoding='utf-8',newline='') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader() #Escribe la primera fila correspondiente a los títulos.
            for pais in lista_paises:
                escritor.writerow(pais) #Traduce el diccionario de Python a formato de texto CSV.
        print("Datos guardados correctamente en el archivo CSV.")
    except Exception as e:
        print(f"Error al guardar en el archivo CSV: {e}")

#------FUNCIÓN: Mostrar países en formato tabular------
def mostrar_paises(lista_paises):
    print(f"\n{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':<18} | {'Continente':<15}")
    print("-" * 75)
    for pais in lista_paises:
        #Cabecera tabulada de la tabla con anchos específicos para una correcta alineación.
        print(f"{pais['nombre']:<20} | {pais['poblacion']:<15,} | {pais['superficie']:<18,} | {pais['continente']:<15}")
    print(f"Total de países registrados: {len(lista_paises)}\n")

#------FUNCIÓN: Agregar un nuevo país (dar de alta uno nuevo)------
def agregar_pais(lista_paises): #Función que permite agregar nuevos países a la lista.
    nombre = solicitar_texto("Ingrese el nombre del país: ")
    #Algoritmo para el control de datos duplicados (países)
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower(): #Estandarizamos cadenas para evitar que se registren nombres repetidos en diferentes formatos.
            print("El país ya existe en la lista. No se puede agregar.")
            return #Si se detecta una colisión de nombres, se aborta la función.
    #Captura de los datos complementarios atravesando las diferentes validaciones.
    poblacion = solicitar_entero_positivo("Ingrese la población del país: ")
    superficie = solicitar_entero_positivo("Ingrese la superficie del país en km²: ")
    continente = solicitar_texto("Ingrese el continente al que pertenece el país: ")

    #Construcción del diccionario
    #Agrupa variables bajo un mapa asociativo (clave-valor) 
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais) #Modificación por reeferencia de la lista original.
    print(f"El país {nombre} ha sido agregado exitosamente.")

#------FUNCIÓN: Actualizar datos de un país------
def actualizar_pais(lista_paises):
    nombre = solicitar_texto("Ingrese el nombre del país que desea actualizar: ")
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Datos actuales del país {nombre}:")
            print(f" - Población: {pais['poblacion']}")
            print(f" - Superficie: {pais['superficie']}")
            print(f" - Continente: {pais['continente']}")
            # Solicitar nuevos datos (de esta manera se cargan los nuevos valores que van a ser lo actualizados).
            nueva_poblacion = solicitar_entero_positivo("Ingrese la nueva población del país: ")
            nueva_superficie = solicitar_entero_positivo("Ingrese la nueva superficie del país en km²: ")
            nuevo_continente = solicitar_texto("Ingrese el nuevo continente al que pertenece el país: ")

            # Actualizar los datos
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            pais["continente"] = nuevo_continente
            print(f"Los datos del país {nombre} han sido actualizados exitosamente.")
            return #Corta la iteración una vez resuelto el cambio.
    print(f"El país {nombre} no fue encontrado en la lista.")

#------FUNCIÓN: Buscar país por nombre------
def buscar_pais(lista_paises):
    #Función que permite al usuario la búsqueda de un país específico de los cargados en el sistema.
    termino_busqueda = solicitar_texto("Ingrese el nombre del país a buscar: ")
    resultados = [pais for pais in lista_paises if termino_busqueda.lower() in pais["nombre"].lower()]

    if resultados:
        mostrar_paises(resultados) #Se reutiliza el formato visual de tablas
    else:
        print("No se encontraron países que coincidan con la búsqueda.")

#------FUNCIÓN: Filtrar países por diferentes opciones------
def filtrar_paises(lista_paises):
    print("Opciones de filtrado: ")
    print("1. Por continente")
    print("2. Por población (rango mínimo y máximo)")
    print("3. Por superficie (rango mínimo y máximo)")
    opcion = solicitar_entero_positivo("Seleccione una de las opciones de filtrado: ")

    resultados = [] #Estructura transitoria para poder almacenar aquellos elementos que pasen los filtros.
    if opcion == 1:
        continente = solicitar_texto("Ingrese el continente a filtrar: ").lower()
        resultados = [pais for pais in lista_paises if pais["continente"].lower() == continente]
    elif opcion == 2:
        poblacion_minima = solicitar_entero_positivo("Ingrese la población mínima: ")
        poblacion_maxima = solicitar_entero_positivo("Ingrese la población máxima: ")
        resultados = [pais for pais in lista_paises if poblacion_minima <= pais["poblacion"] < poblacion_maxima]
    elif opcion == 3:
        superficie_minima = solicitar_entero_positivo("Ingrese la superficie minima en km²: ")
        superficie_maxima = solicitar_entero_positivo("Ingrese la superficie máxima en km²: ")
        resultados = [pais for pais in lista_paises if superficie_minima <= pais["superficie"] < superficie_maxima]
    else:
        print("Opción de filtrado no válida.")
        return
    
    if resultados:
        mostrar_paises(resultados)
    else:
        print("No se encontraron países que coincidan con el filtro seleccionado.")

#------FUNCIÓN: Ordenar países------
def ordenar_paises(lista_paises):
    if not lista_paises:
        print("No hay países para ordenar.")
        return
    #Las diferentes opciones que se pueden elegir para el ordenamiento de datos
    print("Opciones de ordenamiento: ")
    print("Criterio: 1. nombre | 2. población | 3. superficie | 4. continente")
    criterio_opcion = input("Seleccione el criterio de ordenamiento (1-4): ")
    sentido_opcion = input("Seleccione el sentido de ordenamiento (1. ascendente | 2. descendente): ").strip()

    #Validar la opción de ordenamiento
    if sentido_opcion == "2":
        descendente = True
    else:
        descendente = False
    
    #Creamos una función auxiliar de ordenamiento según el critero
    if criterio_opcion == "1":
        def obtener_nombre(pais):
            return pais["nombre"]
        lista_paises.sort(key=obtener_nombre, reverse=descendente)
    
    elif criterio_opcion == "2":
        def obtener_poblacion(pais):
            return pais["poblacion"]
        lista_paises.sort(key=obtener_poblacion, reverse=descendente)
    
    elif criterio_opcion == "3":
        def obtener_superficie(pais):
            return pais["superficie"]
        lista_paises.sort(key=obtener_superficie, reverse=descendente)
    
    elif criterio_opcion == "4":
        def obtener_continente(pais):
            return pais["continente"]
        lista_paises.sort(key=obtener_continente, reverse=descendente)
    #Claúsula de contingencia para entradas que estén fuera del rango de menú iterativo.
    else:
        print("Criterio de ordenamiento no válido.")
        return
    
    #Mostramos el resultado ordenado
    mostrar_paises(lista_paises)

#------FUNCIÓN: Procesamiento y reporte estadístico------
def mostrar_estadisticas(lista_paises):
    """Genera reportes matemáticos: mayor/menor, promedios y conteos por continente."""
    if not lista_paises:
        print("No hay datos suficientes para calcular estadísticas.")
        return
    
    print("\n===REPORTE ESTADÍSTICO===")

    #1. Inicialización de Variables para mayor y menor población
    #Para esto, tomamos como referencia el primer país de la lista.
    
    pais_mayor_poblacion = lista_paises[0]
    pais_menor_poblacion = lista_paises[0]

    #Variables para acumular los totales de población y superficie
    total_poblacion = 0
    total_superficie = 0

    #Diccionario para contar los países por continente
    conteo_continentes = {}

    # Un único bucle for para procesar todo el Dataset
    for pais in lista_paises:
        #Lógica para determinar el mayor y menor
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais
        
        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais
        
        #Acumulación para Promedios
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        #Conteo de continentes
        continente = pais["continente"]
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1
    
    #Cálculo de Promedios Marco Teórico
    cantidad_total = len(lista_paises)
    promedio_poblacion = total_poblacion / cantidad_total
    promedio_superficie = total_superficie / cantidad_total

    #Salida de Resultados
    print(f"Mayor Población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,} habitantes.)")
    print(f"Menor Población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,} habitantes.)")
    print(f"Promedio de Población Global: {promedio_poblacion:,.2f} habitantes.")
    print(f"Promedio de Superficie Global: {promedio_superficie:,.2f} km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f" - {continente}: {cantidad}")
    
    print("----------------------------------------------------")

#------Menú Principal y Arranque------
def menu_principal():
    #Carga inicial del archivo CSV
    lista_paises = cargar_paises()

    while True:
        print("\n---SISTEMA DE GESTIÓN DE PAISES---")
        print("1. Mostrar todos los países")
        print("2. Agregar un país")
        print("3. Actualizar población y superficie")
        print("4. Buscar país por nombre")
        print("5. Filtrar países")
        print("6. Ordenar países")
        print("7. Ver reporte estadístico")
        print("8. Guardar y Salir")

        opcion = input("Seleccione una opcion (1-8): ").strip()

        if opcion == "1":
            if lista_paises:
                mostrar_paises(lista_paises)
            else:
                print("La lista de países en la memoria está vacía.")
        elif opcion == "2":
            agregar_pais(lista_paises)
        elif opcion == "3":
            actualizar_pais(lista_paises)
        elif opcion == "4":
            buscar_pais(lista_paises)
        elif opcion == "5":
            filtrar_paises(lista_paises)
        elif opcion == "6":
            ordenar_paises(lista_paises)
        elif opcion == "7":
            mostrar_estadisticas(lista_paises)
        elif opcion == "8":
            guardar_paises(lista_paises)
            print("Cambios guardados correctamente. Gracias por utilizar el sistema.")
        
        else:
            print("Opción inválida. Intente con un número del 1 al 8.")

if __name__ == "__main__":
    menu_principal()