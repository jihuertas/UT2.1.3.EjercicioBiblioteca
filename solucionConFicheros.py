# -----------------------------
# Gestión de Biblioteca Digital (Parte 2 - Ficheros)
# -----------------------------

import json
import os

# ============================
# FUNCIONES DE FICHEROS
# ============================

def guardar_biblioteca(biblioteca, nombre_fichero):
    """
    Guarda toda la información de la biblioteca en un fichero JSON.
    Si el fichero ya existe, lo sobrescribe.
    """
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as f:
            json.dump(biblioteca, f, indent=4, ensure_ascii=False)
        print(f"💾 Datos guardados correctamente en '{nombre_fichero}'.")
    except Exception as e:
        print(f"⚠️ Error al guardar los datos: {e}")


def cargar_biblioteca(nombre_fichero):
    """
    Carga la biblioteca desde un fichero JSON.
    Si no existe, devuelve una lista vacía.
    """
    if not os.path.exists(nombre_fichero):
        print(f"📁 No se encontró el fichero '{nombre_fichero}'. Se creará una biblioteca nueva.")
        return []

    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            biblioteca = json.load(f)
        print(f"📂 Biblioteca cargada desde '{nombre_fichero}'.")
        return biblioteca
    except json.JSONDecodeError:
        print("⚠️ Error: El fichero existe pero está corrupto o tiene formato incorrecto.")
        return []
    except Exception as e:
        print(f"⚠️ Error al leer el fichero: {e}")
        return []


def exportar_resumen(biblioteca, nombre_fichero):
    """
    Crea un fichero de texto con un resumen legible de todos los libros
    y el número total de préstamos.
    """
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as f:
            f.write("📚 RESUMEN DE LA BIBLIOTECA\n")
            f.write("=" * 50 + "\n\n")
            for libro in biblioteca:
                total_prestamos = sum(libro["prestamos"].values())
                linea = (
                    f"Título: {libro['titulo']} | "
                    f"Autor: {libro['autor']} | "
                    f"Año: {libro['anio']} | "
                    f"Género: {libro['genero']} | "
                    f"Préstamos totales: {total_prestamos}\n"
                )
                f.write(linea)
            f.write("\n" + "=" * 50 + "\n")
        print(f"📝 Resumen exportado correctamente en '{nombre_fichero}'.")
    except Exception as e:
        print(f"⚠️ Error al exportar el resumen: {e}")


# ============================
# FUNCIONES DEL EJERCICIO ANTERIOR
# ============================

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


def prestamo(biblioteca, titulo, usuario):
    """
    Registra un préstamo de un libro por parte de un usuario.
    """
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["prestamos"][usuario] = libro["prestamos"].get(usuario, 0) + 1
            print(f"📚 Préstamo registrado: {usuario} → {libro['titulo']}")
            return
    print(f"⚠️ Libro '{titulo}' no encontrado.")


# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    nombre_fichero = "biblioteca.json"

    # 1. Cargar datos del fichero si existe
    biblioteca = cargar_biblioteca(nombre_fichero)

    # 2. Si está vacía, crear biblioteca inicial
    if not biblioteca:
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
        print("\n📘 Biblioteca creada con libros iniciales.\n")

    # 3. Mostrar catálogo
    print("\n📚 Catálogo actual:")
    mostrar_libros(biblioteca)

    # 4. Simular algunos préstamos
    print("\n🔹 Registrando préstamos de ejemplo...\n")
    prestamo(biblioteca, "1984", "Ana")
    prestamo(biblioteca, "Cien años de soledad", "Luis")
    prestamo(biblioteca, "El Quijote", "Ana")
    prestamo(biblioteca, "El Quijote", "Ana")  # Ana lo pide dos veces

    # 5. Guardar biblioteca actualizada en JSON
    guardar_biblioteca(biblioteca, nombre_fichero)

    # 6. Exportar resumen en fichero de texto
    exportar_resumen(biblioteca, "resumen_biblioteca.txt")

    print("\n✅ Programa finalizado correctamente.\n")


# ============================
# EJECUCIÓN DEL PROGRAMA
# ============================

if __name__ == "__main__":
    main()
