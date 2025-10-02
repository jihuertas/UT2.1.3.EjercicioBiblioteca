# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------

# Funciones

def mostrar_libros(biblioteca):
    for libro in biblioteca:
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['anio']}")
        print(f"Género: {libro['genero']}")
        print("Préstamos:")
        if libro["prestamos"]:
            for usuario, cantidad in libro["prestamos"].items():
                print(f"  - {usuario}: {cantidad}")
        else:
            print("  Ninguno")
        print("-" * 40)


def buscar_por_autor(biblioteca, autor):
    titulos = []
    for libro in biblioteca:
        if libro["autor"].lower() == autor.lower():
            titulos.append(libro["titulo"])
    return titulos


def prestamo(biblioteca, titulo, usuario):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            if usuario in libro["prestamos"]:
                libro["prestamos"][usuario] += 1
            else:
                libro["prestamos"][usuario] = 1
            print(f" Préstamo registrado: {usuario} → {libro['titulo']}")
            return
    print(" Libro no encontrado.")


def libro_mas_popular(biblioteca):
    mas_popular = None
    max_prestamos = -1
    for libro in biblioteca:
        total = sum(libro["prestamos"].values())
        if total > max_prestamos:
            mas_popular = libro
            max_prestamos = total
    return mas_popular


def estadisticas_usuarios(biblioteca):
    estadisticas = {}
    for libro in biblioteca:
        for usuario, cantidad in libro["prestamos"].items():
            if usuario in estadisticas:
                estadisticas[usuario] += cantidad
            else:
                estadisticas[usuario] = cantidad
    return estadisticas


# Programa principal
def main():
    # 1. Crear biblioteca
    biblioteca = [
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "anio": 1967,
            "genero": "Novela",
            "prestamos": {}
        },
        {
            "titulo": "El Quijote",
            "autor": "Miguel de Cervantes",
            "anio": 1605,
            "genero": "Novela",
            "prestamos": {}
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "anio": 1949,
            "genero": "Distopía",
            "prestamos": {}
        },
        {
            "titulo": "La sombra del viento",
            "autor": "Carlos Ruiz Zafón",
            "anio": 2001,
            "genero": "Misterio",
            "prestamos": {}
        },
        {
            "titulo": "El principito",
            "autor": "Antoine de Saint-Exupéry",
            "anio": 1943,
            "genero": "Fábula",
            "prestamos": {}
        }
    ]

    # 2. Mostrar todos los libros
    print("\n Catálogo de la biblioteca:")
    mostrar_libros(biblioteca)

    # 3. Buscar por autor
    autor = input("\n Introduce un autor para buscar: ")
    encontrados = buscar_por_autor(biblioteca, autor)
    if encontrados:
        print(f"Libros de {autor}: {', '.join(encontrados)}")
    else:
        print(f"No se encontraron libros de {autor}.")

    # 4. Simular préstamos
    prestamo(biblioteca, "1984", "Ana")
    prestamo(biblioteca, "1984", "Luis")
    prestamo(biblioteca, "El principito", "Ana")
    prestamo(biblioteca, "El Quijote", "Pedro")
    prestamo(biblioteca, "El Quijote", "Pedro")  # Pedro lo pide dos veces

    # 5. Mostrar libro más popular
    popular = libro_mas_popular(biblioteca)
    if popular:
        print(f"\n El libro más popular es: {popular['titulo']} ({sum(popular['prestamos'].values())} préstamos)")

    # 6. Mostrar estadísticas de usuarios
    print("\n Estadísticas de préstamos:")
    estadisticas = estadisticas_usuarios(biblioteca)
    for usuario, total in estadisticas.items():
        print(f"  - {usuario}: {total}")


# Ejecutar programa
if __name__ == "__main__":
    main()
