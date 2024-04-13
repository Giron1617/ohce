"Permite gestionar y ejecutar pruebas unitarias. -->"
import unittest

import ohce

class testohce(unittest.TestCase):

    def test_salu_6_12(self):

        """
    se definen los test que comprueban el resultado esperado de las funciones en 'ohce.py',
    atravez de la funcion 'self.assertEqual(lo que enviamos, lo que esperamos recibir)'. -->  
    
        """

        nombre = "Juan"
        horas = 8

        resu = ohce.salu(nombre, horas)

        self.assertEqual(resu, "buenos dias Juan")


    def test_salu_12_20(self):
       
        nombre = "Esteban"
        horas = 15

        

        resu  = ohce.salu(nombre, horas)

       
        self.assertEqual(resu, "buenas tardes Esteban")

    def test_salu_20_6(self):
        
        nombre = "Giron"
        horas = 23
        resu = ohce.salu(nombre, horas)

        
        self.assertEqual(resu, "buenas noches Giron")

    """
    Test para la segunda y tercera parte del problema 'OHCE', usando la misma logica que los test anteriores.
    
    """

    def test_ppalin(self):
        palabra = "oto"
        resu  = ohce.pro_p(palabra)

        self.assertEqual(resu, "oto\n bonita palabra")

    def test_stop(self):
        
        palabra = "stop"
        resu= ohce.pro_p(palabra)

       
        self.assertEqual(resu, "adios")     