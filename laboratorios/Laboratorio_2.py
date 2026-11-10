#Maria Belen Hernandez Vasquez
# Mapa de la feria científica
mapa = {
    "E": ["C", "J"],
    "C": ["E", "R", "T"],
    "J": ["E", "S"],
    "R": ["C", "S"],
    "T": ["C", "S"],
    "S": ["J", "R", "T"]
}

nodos = ["E", "C", "J", "R", "T", "S"]

nombres = {
    "E": "Entrada",
    "C": "Exposición de ciencias",
    "J": "Zona de juegos",
    "R": "Robótica",
    "T": "Talleres",
    "S": "Salida"
}


def construir_matriz(mapa, nodos):
    """Construye la matriz de adyacencia a partir de la lista de adyacencia."""
    n = len(nodos)
    matriz = [[0] * n for _ in range(n)]
    indice = {nodo: i for i, nodo in enumerate(nodos)}

    for origen in mapa:
        for destino in mapa[origen]:
            i = indice[origen]
            j = indice[destino]
            matriz[i][j] = 1

    return matriz


def dfs_recursivo(mapa, inicio):
    """DFS recursivo. Retorna la lista del orden de visita."""
    visitados = set()
    orden = []

    def dfs(nodo):
        visitados.add(nodo)
        orden.append(nodo)
        for vecino in mapa[nodo]:
            if vecino not in visitados:
                dfs(vecino)

    dfs(inicio)
    return orden


def dfs_iterativo(mapa, inicio):
    """DFS iterativo con pila. Usa reversed() para mantener el mismo orden."""
    visitados = set()
    orden = []
    pila = [inicio]

    while pila:
        nodo = pila.pop()
        if nodo in visitados:
            continue
        visitados.add(nodo)
        orden.append(nodo)
        for vecino in reversed(mapa[nodo]):
            if vecino not in visitados:
                pila.append(vecino)

    return orden


def validar_nodo(texto):
    """Valida y normaliza el nodo (acepta mayúsculas o minúsculas)."""
    nodo = texto.strip().upper()
    if nodo in mapa:
        return nodo
    return None


def mostrar_menu():
    print("\n=== MAPA DE LA FERIA CIENTÍFICA ===")
    print("1. Ver conexiones de un espacio")
    print("2. Ver matriz de adyacencia")
    print("3. Recorrer con DFS recursivo")
    print("4. Recorrer con DFS iterativo")
    print("5. Consultar si hay un pasillo directo")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            espacio = input("Espacio: ")
            nodo = validar_nodo(espacio)
            if nodo is None:
                print("Ese espacio no existe en el mapa.")
            else:
                vecinos = ", ".join(mapa[nodo])
                print(f"{nodo} · {nombres[nodo]} se conecta con: {vecinos}")

        elif opcion == "2":
            matriz = construir_matriz(mapa, nodos)
            # Encabezado
            print("\n  " + " ".join(nodos))
            for i, nodo in enumerate(nodos):
                fila = " ".join(str(matriz[i][j]) for j in range(len(nodos)))
                print(f"{nodo} {fila}")

        elif opcion == "3":
            inicio_txt = input("Nodo inicial: ")
            inicio = validar_nodo(inicio_txt)
            if inicio is None:
                print("Ese espacio no existe en el mapa.")
            else:
                recorrido = dfs_recursivo(mapa, inicio)
                print(" -> ".join(recorrido))

        elif opcion == "4":
            inicio_txt = input("Nodo inicial: ")
            inicio = validar_nodo(inicio_txt)
            if inicio is None:
                print("Ese espacio no existe en el mapa.")
            else:
                recorrido = dfs_iterativo(mapa, inicio)
                print(" -> ".join(recorrido))

        elif opcion == "5":
            origen_txt = input("Nodo origen: ")
            destino_txt = input("Nodo destino: ")
            origen = validar_nodo(origen_txt)
            destino = validar_nodo(destino_txt)

            if origen is None or destino is None:
                print("Ese espacio no existe en el mapa.")
            else:
                matriz = construir_matriz(mapa, nodos)
                i = nodos.index(origen)
                j = nodos.index(destino)
                if matriz[i][j] == 1:
                    print(f"Existe un pasillo directo entre {origen} y {destino}.")
                else:
                    print(f"No existe un pasillo directo entre {origen} y {destino}.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
