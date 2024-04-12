"Permite gestionar y ejecutar pruebas unitarias. -->"
import unittest

import ohce

class testohce(unittest.TestCase):

    def test_salu_6_12(self):

        """
    se definen los test que comprueban el resultado esperado de las funciones en 'ohce.py',
    atravez de la funcion 'self.assertEqual(lo que enviamos, lo que esperamos recibir)'. -->  
    
        """

        nombre = "juan"
        horas = 8

        resu = ohce.salu(nombre, horas)

        self.assertEqual(resu, "buenos dias juan")