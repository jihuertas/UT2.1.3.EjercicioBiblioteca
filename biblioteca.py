# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------

# Funciones

def mostrar_libros(biblioteca):
    # Recorre la lista y muestra la información de cada libro
    pass


def buscar_por_autor(biblioteca, autor):
    # Devuelve una lista con los títulos de un autor dado
    pass


def prestamo(biblioteca, titulo, usuario):
    # Registra un préstamo de un libro por un usuario
    pass


def libro_mas_popular(biblioteca):
    # Devuelve el libro con más préstamos totales
    pass


def estadisticas_usuarios(biblioteca):
    # Devuelve un diccionario con total de préstamos por usuario
    pass


# Programa principal
def main():
    # 1. Crear biblioteca con al menos 5 libros
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
        # Añadir más libros aquí...
    ]

    # 2. Mostrar todos los libros
    # 3. Buscar por autor (pedir al usuario un nombre)
    # 4. Simular préstamos
    # 5. Mostrar el libro más popular
    # 6. Mostrar estadísticas de usuarios


# Ejecutar programa
if __name__ == "__main__":
    main()
