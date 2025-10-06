## **Gestión de Biblioteca Digital (Parte 2 — Uso de Ficheros)**

En este ejercicio continuarás desarrollando el programa de **Gestión de Biblioteca Digital** del ejercicio anterior.
Esta vez, añadirás la posibilidad de **guardar** y **cargar** la información de los libros y los préstamos desde ficheros.

---

## Objetivo del ejercicio

Implementar funciones que permitan **persistir los datos** de la biblioteca usando **ficheros de texto** y/o **ficheros JSON**, de modo que la información no se pierda al cerrar el programa.

---

## Nuevas funcionalidades a implementar

Debes añadir las siguientes funciones al programa anterior:

1. **`guardar_biblioteca(biblioteca, nombre_fichero)`**

   * Guarda toda la información de la biblioteca en un fichero JSON.
   * Si el fichero ya existe, debe sobrescribirse.
   * Muestra un mensaje confirmando que los datos se han guardado correctamente.

2. **`cargar_biblioteca(nombre_fichero)`**

   * Lee el fichero JSON y devuelve la lista de libros (la estructura completa).
   * Si el fichero no existe, devuelve una lista vacía y muestra un mensaje de aviso.

3. **`exportar_resumen(biblioteca, nombre_fichero)`**

   * Crea un fichero de texto (.txt) que contenga un **resumen legible** con todos los libros y sus préstamos.
   * Cada línea debe tener el siguiente formato:

     ```
     Título: El Quijote | Autor: Cervantes | Año: 1605 | Préstamos totales: 3
     ```

---

## Programa principal

En el programa principal debes añadir:

1. **Intentar cargar** los datos de la biblioteca desde un fichero `biblioteca.json`.
2. Si el fichero no existe, **crear una biblioteca nueva** con algunos libros iniciales.
3. Guardar los datos actualizados en `biblioteca.json` al final del programa.
4. Exportar el resumen en un fichero `resumen_biblioteca.txt`.

---

## Requisitos técnicos

* Usa el módulo **`json`** de Python para leer y escribir ficheros JSON.
* Usa el modo de apertura adecuado en `open()` (`"w"`, `"r"`, `"a"` según el caso).
* El programa debe manejar correctamente los **errores** de lectura o inexistencia de archivos (por ejemplo, usando `try...except`).
* Se deben mantener todas las funcionalidades del ejercicio anterior (búsqueda, préstamos, estadísticas…).

---

## Pistas

* Para guardar en JSON:

  ```python
  import json
  with open("biblioteca.json", "w", encoding="utf-8") as f:
      json.dump(biblioteca, f, indent=4, ensure_ascii=False)
  ```
* Para leer desde JSON:

  ```python
  with open("biblioteca.json", "r", encoding="utf-8") as f:
      biblioteca = json.load(f)
  ```
* Para escribir un resumen de texto:

  ```python
  with open("resumen_biblioteca.txt", "w", encoding="utf-8") as f:
      f.write("Título: El Quijote | Autor: Cervantes | Año: 1605 | Préstamos totales: 3\n")
  ```

---

