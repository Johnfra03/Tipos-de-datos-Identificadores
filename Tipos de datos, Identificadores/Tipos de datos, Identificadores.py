# Programa para gestionar el registro de libros en una biblioteca

# Función para agregar un libro a la biblioteca
def agregar_libro(biblioteca, titulo_libro, autor_libro, anio_publicacion, genero_libro, numero_paginas):
    """
    Agrega un libro al registro de la biblioteca con más detalles.

    Parámetros:
    titulo_libro (str): El título del libro.
    autor_libro (str): El autor del libro.
    anio_publicacion (int): El año de publicación del libro.
    genero_libro (str): El género del libro.
    numero_paginas (int): El número de páginas del libro.
    """
    libro = {
        "titulo": titulo_libro,
        "autor": autor_libro,
        "anio": anio_publicacion,
        "genero": genero_libro,
        "paginas": numero_paginas
    }
    biblioteca.append(libro)
    print(f"Libro '{titulo_libro}' de {autor_libro} agregado a la biblioteca.")


# Función para buscar un libro por su título
def buscar_libro(biblioteca, titulo_libro):
    """
    Busca un libro en la biblioteca por su título.

    Parámetros:
    titulo_libro (str): El título del libro que se desea buscar.

    Retorna:
    dict: El libro encontrado, o None si no se encuentra.
    """
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_libro.lower():
            return libro
    return None


# Variables
biblioteca_registro = []  # Lista para almacenar los libros en la biblioteca

# Agregar algunos libros con más detalles
agregar_libro(biblioteca_registro, "1984", "George Orwell", 1949, "Distopía", 328)
agregar_libro(biblioteca_registro, "El principito", "Antoine de Saint-Exupéry", 1943, "Fábula", 96)
agregar_libro(biblioteca_registro, "Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo Mágico", 417)
agregar_libro(biblioteca_registro, "Matar a un ruiseñor", "Harper Lee", 1960, "Ficción", 281)
agregar_libro(biblioteca_registro, "Orgullo y prejuicio", "Jane Austen", 1813, "Romántico", 279)

# Solicitar al usuario el título de libro para buscar
titulo_buscar = input("Ingrese el título del libro que desea buscar: ")  # Entrada del usuario para buscar el libro
libro_encontrado = buscar_libro(biblioteca_registro, titulo_buscar)

# Mostrar el resultado de la búsqueda
if libro_encontrado:
    print(f"\nEl libro '{libro_encontrado['titulo']}' fue encontrado. Autor: {libro_encontrado['autor']}, "
          f"Año: {libro_encontrado['anio']}, Género: {libro_encontrado['genero']}, Páginas: {libro_encontrado['paginas']}")
else:
    print(f"\nEl libro '{titulo_buscar}' no se encuentra en la biblioteca.")
