import heapq

# Definición de la clase Nodo para representar los nodos del grafo
class Nodo:
    def __init__(self, estado, costo, camino):
        self.estado = estado
        self.costo = costo
        self.camino = camino  # Lista para almacenar el camino hasta este nodo

    # Comparación de nodos basada en el costo
    def __lt__(self, otro):
        return self.costo < otro.costo

# Función de búsqueda de costo uniforme
def busqueda_costo_uniforme(estado_inicial, objetivo, graf):
    nodos_frontera = []
    nodos_visitados = set()

    # Inicialización con el nodo inicial
    nodo_inicial = Nodo(estado_inicial, 0, [estado_inicial])
    heapq.heappush(nodos_frontera, nodo_inicial)

    while nodos_frontera:
        # Seleccionar el nodo con menor costo de la frontera
        nodo_actual = heapq.heappop(nodos_frontera)

        # Verificar si el nodo actual es el objetivo
        if nodo_actual.estado == objetivo:
            return nodo_actual.camino, nodo_actual.costo

        # Agregar el nodo actual a los nodos visitados
        nodos_visitados.add(nodo_actual.estado)

        # Expandir el nodo actual
        for hijo, costo in graf[nodo_actual.estado].items():
            if hijo not in nodos_visitados:
                nuevo_costo = nodo_actual.costo + costo
                nuevo_camino = nodo_actual.camino + [hijo]  # Agregar el hijo al camino
                nuevo_nodo = Nodo(hijo, nuevo_costo, nuevo_camino)
                heapq.heappush(nodos_frontera, nuevo_nodo)

    # Si no se encuentra la solución, devolver None
    return None, None

# Ejemplo de grafo y ejecución de la búsqueda
grafo = {
    'EDO.MEX': {'SLP': 513, 'CDMX': 125},
    'CDMX': {'SLP': 423, 'MICHOACAN': 491},
    'SLP': {'MICHOACAN': 355, 'SONORA': 603, 'MONTERREY': 313, 'GUADALAJARA': 437, 'HIDALGO': 599, 'QRO': 203, 'PUEBLA': 514},
    'MICHOACAN': {'SONORA': 346, 'MONTERREY': 296},
    'QRO': {'HIDALGO': 390},
    'MONTERREY': {'SONORA': 296},
    'GUADALAJARA': {},
    'SONORA': {},
    'HIDALGO': {},
    'PUEBLA': {}
}

estado_inicial = 'EDO.MEX'
objetivo = 'HIDALGO'

camino, costo = busqueda_costo_uniforme(estado_inicial, objetivo, grafo)

if camino:
    print("Solucion:", camino)
    print("Costo:", costo)
else:
    print("No se encontró un camino hacia", objetivo)