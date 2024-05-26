import unittest
import json
import os
from libreria import Libreria  # Asumimos que el código de la clase Libreria está en un archivo llamado libreria.py

class TestLibreria(unittest.TestCase):

    def setUp(self):
        """ Configuración inicial para cada prueba. """
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.anadir_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 1605)

    def test_anadir_libro(self):
        """ Prueba para añadir un libro. """
        resultado = self.libreria.anadir_libro("1984", "George Orwell", "Distopía", 1949)
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 3)

    def test_buscar_libro(self):
        """ Prueba para buscar un libro por título. """
        resultados = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]['autor'], "Gabriel García Márquez")

        resultados = self.libreria.buscar_libro("Libro inexistente")
        self.assertEqual(len(resultados), 0)

    def test_buscar_por_autor(self):
        """ Prueba para buscar libros por autor. """
        resultados = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]['titulo'], "Cien años de soledad")

        resultados = self.libreria.buscar_por_autor("Autor inexistente")
        self.assertEqual(len(resultados), 0)

    def test_eliminar_libro(self):
        """ Prueba para eliminar un libro por título. """
        resultado = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 1)

        resultado = self.libreria.eliminar_libro("Libro inexistente")
        self.assertEqual(resultado, "Libro no encontrado")
        self.assertEqual(len(self.libreria.libros), 1)

    def test_guardar_libros(self):
        """ Prueba para guardar libros en un archivo JSON. """
        archivo = 'test_libreria.json'
        resultado = self.libreria.guardar_libros(archivo)
        self.assertEqual(resultado, "Libros guardados")
        self.assertTrue(os.path.exists(archivo))

        with open(archivo, 'r') as f:
            libros_guardados = json.load(f)
        self.assertEqual(len(libros_guardados), 2)

        os.remove(archivo)  # Limpiar el archivo de prueba

    def test_cargar_libros(self):
        """ Prueba para cargar libros desde un archivo JSON. """
        archivo = 'test_libreria.json'
        self.libreria.guardar_libros(archivo)

        nueva_libreria = Libreria()
        resultado = nueva_libreria.cargar_libros(archivo)
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(len(nueva_libreria.libros), 2)

        os.remove(archivo)  # Limpiar el archivo de prueba

        resultado = nueva_libreria.cargar_libros('archivo_inexistente.json')
        self.assertEqual(resultado, "Archivo no encontrado")

    def tearDown(self):
        """ Limpieza después de cada prueba. """
        pass

if __name__ == '__main__':
    unittest.main()
