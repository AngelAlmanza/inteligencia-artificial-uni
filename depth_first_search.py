class GrafoDirigido:
    def __init__(self):
        # Un diccionario para almacenar los vértices del grafo
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, inicio, fin):
        # Agrega una arista al grafo, asumiendo que los vértices ya existen
        self.vertices[inicio].append(fin)

    def mostrar_matriz_de_adyacencia(grafo):
        vertices = list(grafo.vertices.keys())
        matriz = [[0] * len(vertices) for _ in range(len(vertices))]

        for i in range(len(vertices)):
            for vecino in grafo.vertices[vertices[i]]:
                j = vertices.index(vecino)
                matriz[i][j] = 1

        print("   " + " ".join(vertices))
        for i in range(len(vertices)):
            print(vertices[i] + " " + " ".join(map(str, matriz[i])))


def DFS(grafo, inicio, objetivo, visitados, descubiertos, padres):
    if inicio == objetivo:
        # Hemos encontrado el nodo objetivo
        return True

    # Marcamos el nodo como descubierto
    descubiertos.add(inicio)

    # Recorremos todos los vertices adyacentes
    for vecino in grafo.vertices[inicio]:
        # Verificamos que este vertice no haya sido dibujado
        if vecino not in visitados:
            padres[vecino] = inicio
            # Verificamos que este vertice no haya sido descubierto
            if vecino not in descubiertos:
                # Repetimos el proceso de manera recursiva hasta que no haya mas vertices hijos o adyacentes
                if DFS(grafo, vecino, objetivo, visitados, descubiertos, padres):
                    return True

    # Marcamos el nodo como visitado después de procesarlo completamente
    visitados.add(inicio)
    return False


def obtener_camino(padres, inicio, objetivo):
    camino = [objetivo]
    while objetivo != inicio:
        objetivo = padres[objetivo]
        camino.insert(0, objetivo)
    return camino


# Ejemplo
if __name__ == "__main__":
    grafo = GrafoDirigido()

    #Agregamos vértices y aristas al grafo dirigido
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")

    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("D", "E")
    grafo.agregar_arista("C", "E")

    inicio = "A"
    objetivo = "E"

    visitados = set()
    descubiertos = set()
    padres = {}

    if DFS(grafo, inicio, objetivo, visitados, descubiertos, padres):
        camino = obtener_camino(padres, inicio, objetivo)
        print(f"Camino desde {inicio} hasta {objetivo}: {camino}")
        grafo.mostrar_matriz_de_adyacencia()
    else:
        print(f"No se encontró un camino desde {inicio} hasta {objetivo}")
