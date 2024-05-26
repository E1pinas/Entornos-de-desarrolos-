# Entornos-de-desarrolos-
Clase Libreria
La clase Libreria es una implementación que gestiona una colección de libros. Aquí tienes un resumen de su funcionalidad:

Atributo:

libros: Lista de diccionarios donde cada diccionario representa un libro con atributos como título, autor, género y año.
Métodos:

__init__: Inicializa la lista de libros.
anadir_libro(titulo, autor, genero, anio): Añade un libro a la librería.
buscar_libro(titulo): Busca un libro por su título.
buscar_por_autor(autor): Busca libros por un autor específico.
eliminar_libro(titulo): Elimina un libro por su título.
guardar_libros(archivo): Guarda la lista de libros en un archivo JSON.
cargar_libros(archivo): Carga la lista de libros desde un archivo JSON.

Verificación de Funcionalidad: Las pruebas unitarias aseguran que cada método de la clase Libreria funcione correctamente en diversos escenarios, incluyendo casos típicos y casos extremos.

Detección Temprana de Errores: Las pruebas ayudan a detectar errores en el código temprano en el ciclo de desarrollo, lo que facilita su corrección antes de que se conviertan en problemas mayores.

Regresión y Mantenimiento: Las pruebas unitarias permiten verificar que nuevas modificaciones en el código no introduzcan errores o afecten la funcionalidad existente, ayudando a mantener la calidad del software a lo largo del tiempo.

Documentación y Claridad: Las pruebas unitarias también sirven como documentación del comportamiento esperado de la clase Libreria, proporcionando ejemplos claros de cómo deben funcionar sus métodos.
