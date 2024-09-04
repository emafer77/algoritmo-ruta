matriz =[
     [-3, -2, 1,2],
    [2, "I", 2,-1],
    [2, -2, -2 ,"F"],
    [2, -2, -2 ,-1]
]


"""
ESTA MATRIZ A UN LA PROCESA EN MI PC
matriz = [
    [-3, -2, 1, 3, -7, -1],
    [2, "I", 2, -3, -8, 1],
    [2, -2, -2, -4, 5, 2],
    [-1, -3, -3, 2, 6, -3],
    [-4, -3, 2, 1, 7, -1],
    [-4, -3, 2, 1, 7, "F"],
   
]"""

"""
SE BUGUEA YA QUE EL MAXIMO  QUE SE PUEDE PROCESAR ES 6X6
matriz = [
    [-3, -3, 2,-3,3,-2,-2,1,2,0,2,0,1],
    [2,3,"I",-1,-1,3,2,0,-3,-3,2,2,1],
    [1,-3,-3,2,3,1,3,3,2,1,-2,-2,3],
    [0,0,3,0,3,-3,-2,-3,0,2,2,1,1],
    [2,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],
    [0,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0],
    [0,3,2,0,1,1,2,3,-1,-3,0,0,-2],
    [3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
    [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],
    [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],
    [-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],
    [-1,0,1,2,1,0,"F",0,-3,3,3,-2,-1],
    [1,-3,1,0,1,2,3,1,-2,3,3,0,3]]
"""

# Dimensiones de la matriz
filas = len(matriz)
columnas = max(len(fila) for fila in matriz)

# Función para encontrar una posición en la matriz
def encontrar_posicion(valor):
    for i in range(filas):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Función para verificar si una coordenada está dentro de los límites y no ha sido visitada
def es_valida(i, j, visitadas):
    return (0 <= i < filas and 0 <= j < len(matriz[i]) and (i, j) not in visitadas)

# DFS para encontrar todas las rutas posibles y sus contadores
def buscar_rutas(i, j, contador, visitadas, ruta_actual, mejor_contador, peor_contador, mejor_ruta, peor_ruta):
    # Si llegamos a la posición final, almacenamos el contador y la ruta
    if matriz[i][j] == "F":
        rutas.append((contador, ruta_actual[:]))
        # Actualizamos la mejor ruta
        if mejor_contador[0] is None or contador < mejor_contador[0]:
            mejor_contador[0] = contador
            mejor_ruta[0] = ruta_actual[:]
        # Actualizamos la peor ruta
        if peor_contador[0] is None or contador > peor_contador[0]:
            peor_contador[0] = contador
            peor_ruta[0] = ruta_actual[:]
        return

    # Movimientos posibles: derecha, izquierda, abajo, arriba
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for mov in movimientos:
        nueva_i, nueva_j = i + mov[0], j + mov[1]
        if es_valida(nueva_i, nueva_j, visitadas):
            # Valor de la celda actual
            valor_celda = matriz[nueva_i][nueva_j]
            # Si el valor es un número, actualizamos el contador
            if isinstance(valor_celda, (int, float)):
                nuevo_contador = contador + valor_celda
            else:
                nuevo_contador = contador  # No incrementa si no es un número
            
            # Añadimos la posición actual a las visitadas y a la ruta
            visitadas.append((nueva_i, nueva_j))
            ruta_actual.append((nueva_i, nueva_j))
            # Continuamos la búsqueda desde la nueva posición
            buscar_rutas(nueva_i, nueva_j, nuevo_contador, visitadas, ruta_actual, mejor_contador, peor_contador, mejor_ruta, peor_ruta)
            # Retrocedemos para probar otra ruta
            visitadas.pop()
            ruta_actual.pop()

# Posiciones inicial y final
posicion_inicial = encontrar_posicion("I")
posicion_final = encontrar_posicion("F")

# Lista para almacenar las rutas y sus contadores
rutas = []

# Variables para almacenar la mejor y la peor ruta
mejor_contador = [None]
peor_contador = [None]
mejor_ruta = [[]]
peor_ruta = [[]]

# Iniciar búsqueda desde la posición inicial
if posicion_inicial and posicion_final:
    i_inicial, j_inicial = posicion_inicial
    buscar_rutas(i_inicial, j_inicial, 0, [(i_inicial, j_inicial)], [(i_inicial, j_inicial)], mejor_contador, peor_contador, mejor_ruta, peor_ruta)

    # Mostrar la mejor y la peor ruta
    if mejor_ruta[0]:
        print(f"La mejor ruta es {mejor_ruta[0]} con un contador de {mejor_contador[0]}")
    else:
        print("No se encontró ninguna ruta de 'I' a 'F'.")
    
    if peor_ruta[0]:
        print(f"La peor ruta es {peor_ruta[0]} con un contador de {peor_contador[0]}")
    else:
        print("No se encontró ninguna ruta de 'I' a 'F'.")
else:
    print("No se encontraron las posiciones inicial y/o final en la matriz.")