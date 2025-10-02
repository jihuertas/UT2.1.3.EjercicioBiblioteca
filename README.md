# UT2.3.EjercicioBiblioteca


## **Gestión de Biblioteca Digital**

Se quiere crear un programa en **Python** para gestionar una pequeña **biblioteca digital**. La biblioteca almacena información sobre los libros y permite consultar y organizar sus datos.

---

## Estructura de datos

* Los libros estarán guardados en una **lista de diccionarios**.
* Cada libro será un diccionario con las siguientes claves:

  * `"titulo"`: título del libro (cadena de texto).
  * `"autor"`: autor del libro (cadena de texto).
  * `"anio"`: año de publicación (entero).
  * `"genero"`: género literario (cadena de texto).
  * `"prestamos"`: un diccionario donde las claves son nombres de usuarios y los valores son el número de veces que cada usuario ha pedido prestado el libro.

Ejemplo de un libro:

```python
{
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "anio": 1967,
    "genero": "Novela",
    "prestamos": {"Ana": 2, "Luis": 1}
}
```

---

## 🔧 Funcionalidades a implementar

Debes crear las siguientes funciones:

1. **`mostrar_libros(biblioteca)`**

   * Recorre la lista de libros y muestra toda la información de cada uno.

2. **`buscar_por_autor(biblioteca, autor)`**

   * Devuelve una lista con los títulos de todos los libros de un autor determinado.

3. **`prestamo(biblioteca, titulo, usuario)`**

   * Registra que un usuario ha pedido prestado un libro.
   * Si el libro ya fue prestado por ese usuario, suma 1 al contador.
   * Si es la primera vez, añade al usuario en el diccionario de `"prestamos"`.

4. **`libro_mas_popular(biblioteca)`**

   * Devuelve el libro con **mayor número total de préstamos** (sumando los préstamos de todos los usuarios).

5. **`estadisticas_usuarios(biblioteca)`**

   * Crea y devuelve un diccionario donde:

     * Las claves son los nombres de los usuarios.
     * Los valores son el número total de préstamos que cada usuario ha hecho en la biblioteca (recorriendo todos los libros).

---

## Programa principal

En el programa principal deberás:

1. Crear una lista de al menos **5 libros** con datos realistas.
2. Mostrar todos los libros con `mostrar_libros`.
3. Preguntar al usuario por un autor y mostrar los títulos encontrados.
4. Simular algunos préstamos de libros por parte de distintos usuarios.
5. Mostrar el libro más popular.
6. Mostrar las estadísticas de préstamos por usuario.

---

## Requisitos técnicos

* El código debe estar estructurado en **funciones**.
* Se deben usar **listas y diccionarios anidados**.
* Para recorrer la información se usarán bucles `for`.
* El **programa principal** debe demostrar todas las funcionalidades pedidas.

---

¿Quieres que también te lo prepare con **formato de hoja de ejercicios para alumnado** (con apartados tipo “Ejercicio 1, Ejercicio 2…”) para que sea aún más didáctico?
