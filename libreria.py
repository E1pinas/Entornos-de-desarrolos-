import json

class Libreria:
    """
    Una clase utilizada para representar una librería.

    Atributos
    ----------
    libros : list
        una lista de diccionarios que representan los libros en la librería

    Métodos
    -------
    anadir_libro(titulo, autor, genero, anio):
        Añade un libro a la librería.
    buscar_libro(titulo):
        Busca un libro por su título.
    buscar_por_autor(autor):
        Busca libros por un autor dado.
    eliminar_libro(titulo):
        Elimina un libro por su título.
    guardar_libros(archivo):
        Guarda la lista de libros en un archivo JSON.
    cargar_libros(archivo):
        Carga la lista de libros desde un archivo JSON.
    """

    def __init__(self):
        """Inicializa la librería con una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la librería.

        Parámetros:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        genero (str): El género del libro.
        anio (int): El año de publicación del libro.

        Retorna:
        str: Mensaje de confirmación de que el libro ha sido añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Parámetros:
        titulo (str): El título del libro a buscar.

        Retorna:
        list: Una lista de libros que coinciden con el título dado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por un autor dado.

        Parámetros:
        autor (str): El nombre del autor a buscar.

        Retorna:
        list: Una lista de libros que coinciden con el autor dado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.

        Parámetros:
        titulo (str): El título del libro a eliminar.

        Retorna:
        str: Mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON.

        Parámetros:
        archivo (str): El nombre del archivo donde se guardarán los libros.

        Retorna:
        str: Mensaje de confirmación de que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la lista de libros desde un archivo JSON.

        Parámetros:
        archivo (str): El nombre del archivo desde el cual se cargarán los libros.

        Retorna:
        str: Mensaje de confirmación de que los libros han sido cargados o de error si el archivo no se encuentra.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


# Crear una instancia de la clase Libreria
mi_libreria = Libreria()

# Añadir un libro a la librería
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)

# Guardar los libros en un archivo JSON
mi_libreria.guardar_libros('libreria.json')

# Cargar los libros desde un archivo JSON y mostrar el mensaje resultante
print(mi_libreria.cargar_libros('libreria.json'))

# Buscar libros por el autor "Gabriel García Márquez" y mostrar los resultados
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))
