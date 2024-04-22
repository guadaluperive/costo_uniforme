from flask import Flask, render_template, request
import operator

# Clase Nodo para representar cada estado
class Nodo:
    def __init__(self, nombre, costo, padre=None):
        self.nombre = nombre
        self.costo = costo
        self.padre = padre

    def __lt__(self, other):
        return self.costo < other.costo

    def __eq__(self, other):
        return self.nombre == other.nombre


# Función para obtener hijos de un nodo
def obtener_hijos(nodo):
    # Código para obtener hijos
    if nodo.nombre == "EDO.MEX":
        return [
            Nodo("CDMX", 125, nodo),
            Nodo("SLP", 513, nodo)
        ]
    elif nodo.nombre == "CDMX":
        return [
            Nodo("SLP", 513, nodo),
            Nodo("MICHOACAN", 616, nodo)
        ]
    elif nodo.nombre == "SLP":
        return [
            Nodo("MICHOACAN", 616, nodo),
            Nodo("SONORA", 1116, nodo),
            Nodo("MONTERREY", 826, nodo),
            Nodo("GUADALAJARA", 950, nodo),
            Nodo("HIDALGO", 1112, nodo),
            Nodo("QRO.", 716, nodo),
            Nodo("PUEBLA", 1027)
        ]
    elif nodo.nombre == "MICHOACAN":
        return [
            Nodo("SONORA", 962, nodo),
            Nodo("MONTERREY", 925, nodo)
        ]
    elif nodo.nombre == "QRO.":
        return [Nodo("HIDALGO", 1106, nodo)]
    elif nodo.nombre == "MONTERREY":
        return [
            Nodo("SONORA", 1122, nodo),
            Nodo("QRO.", 1220, nodo)
        ]
    elif nodo.nombre == "GUADALAJARA":
        return []
    elif nodo.nombre == "SONORA":
        return []

    return []

# Función para reconstruir el camino desde el nodo solución hasta el nodo inicial
def reconstruir_camino(nodo):
    camino = []
    actual = nodo
    while actual:
        camino.append(actual.nombre)
        actual = actual.padre
    return camino[::-1]

# Búsqueda de costo uniforme
def busca_costo_uniforme():
    nodo_inicial = Nodo("EDO.MEX", 0)
    nodos_frontera = [nodo_inicial]
    nodos_visitados = []

    while nodos_frontera:
        nodos_frontera.sort()

        nodo_actual = nodos_frontera.pop(0)

        if nodo_actual.nombre == "HIDALGO":
            return reconstruir_camino(nodo_actual)

        nodos_visitados.append(nodo_actual)

        hijos = obtener_hijos(nodo_actual)

        for hijo in hijos:
            if hijo not in nodos_frontera or hijo not in nodos_visitados:
                nodos_frontera.append(hijo)
    return []

# Crear aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para la búsqueda y resultado
@app.route("/buscar", methods=["POST"])
def buscar():
    camino = busca_costo_uniforme()  # Buscar el camino a HIDALGO
    return render_template("resultado.html", camino=camino)  # Mostrar resultado

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
