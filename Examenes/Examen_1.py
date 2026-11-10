#Maria Belen Hernandez Vasquez / CCP


class Contenido:
    def __init__(self, titulo, calificacion):
        self.titulo = titulo
        self._calificacion = 0
        self.calificacion = calificacion

    @property
    def calificacion(self):
        return self._calificacion

    @calificacion.setter
    def calificacion(self, valor):
        if valor < 0:
            self._calificacion = 0
        else:
            self._calificacion = valor

    def __str__(self):
        return f"{self.titulo} (Calificacion: {self.calificacion})"

    def __lt__(self, other):
        return self.calificacion < other.calificacion


class Pelicula(Contenido):
    def __init__(self, titulo, calificacion, duracion_minutos):
        super().__init__(titulo, calificacion)
        self.duracion_minutos = duracion_minutos

    def __str__(self):
        return f"Pelicula : {self.titulo}, Duracion {self.duracion_minutos} min , Calificacion: {self.calificacion}"


class Serie(Contenido):
    def __init__(self, titulo, calificacion, temporadas):
        super().__init__(titulo, calificacion)
        self.temporadas = temporadas

    def __str__(self):
        return f"Serie: {self.titulo}, Temporadas {self.temporadas} , Calificacion {self.calificacion}"

    @classmethod
    def desde_cadena(cls, texto):
        partes = texto.split(",")
        titulo = partes[0].strip()
        temporadas = int(partes[1].strip())
        calificacion = float(partes[2].strip())
        return cls(titulo, calificacion, temporadas)


class Playlist:
    def __init__(self):
        self.contenidos = []

    def agregar_contenido(self, contenido):
        self.contenidos.append(contenido)

    def vaciar_playlist(self):
        self.contenidos = []

    def mostrar_playlist(self):
        for obj in self.contenidos:
            print(obj)

    def ordenar_por_calificacion(self):
        return sorted(self.contenidos, reverse=True)

    def calcular_calificacion_promedio(self):
        if len(self.contenidos) == 0:
            return 0
        suma = 0
        for c in self.contenidos:
            suma = suma + c.calificacion
        return suma / len(self.contenidos)


def main():
    # 1 
    c1 = Contenido("Documental", 7.5)
    p1 = Pelicula("Inception", 8.8, 148)
    s1 = Serie("Breaking Bad", 9.5, 5)

    # 2 
    s2 = Serie.desde_cadena("Stranger Things, 4, 4.8")

    # 3
    lista = Playlist()
    lista.agregar_contenido(c1)
    lista.agregar_contenido(p1)
    lista.agregar_contenido(s1)
    lista.agregar_contenido(s2)

    # 4 
    print("=== Playlist ===")
    lista.mostrar_playlist()

    # 5 
    print("\n=== Asignando calificación negativa a Inception ===")
    p1.calificacion = -5
    print(p1)

    # 6
    print("\n=== Ordenado por calificación (mayor a menor) ===")
    ordenados = lista.ordenar_por_calificacion()
    for c in ordenados:
        print(c)

    # 7
    print(f"\nCalificación promedio: {lista.calcular_calificacion_promedio():.2f}")

    # 8
    print("\n=== Vaciando la playlist ===")
    lista.vaciar_playlist()
    print("Contenidos restantes:", lista.contenidos)
    print("Promedio después de vaciar:", lista.calcular_calificacion_promedio())


if __name__ == "__main__":
    main()
