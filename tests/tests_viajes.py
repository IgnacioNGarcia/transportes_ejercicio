import unittest
from src.factory.Creador import CreadorTransporte
from src.models.Auto import Auto
from src.models.Dron import Dron
from src.factory.Creador_autos import CreadorAutos
from src.factory.Creador_drones import CreadorDrones
#Test: python -m unittest tests/tests_viajes.py -v

class TestViajes(unittest.TestCase):
    def test_creacion_de_transporte_auto(self):
        input_vehiculo = "auto"
        creador = CreadorTransporte.get_creador(input_vehiculo)
        self.assertIsInstance(creador, CreadorAutos)
        
    def test_creacion_de_transporte_dron(self):
        input_vehiculo = "dron"
        creador = CreadorTransporte.get_creador(input_vehiculo)
        self.assertIsInstance(creador, CreadorDrones)
        
    def test_creacion_de_transporte_invalido(self):
        input_vehiculo = "avion"
        with self.assertRaises(ValueError):
            creador = CreadorTransporte.get_creador(input_vehiculo)
            creador.get_transporte()

    def test_viaje_en_auto(self):
        input_vehiculo = "auto"
        creador = CreadorTransporte.get_creador(input_vehiculo)
        transporte = creador.get_transporte()
        self.assertEqual(transporte.transportar("Buenos Aires", "Mexico"), "🚗 Transportando de Buenos Aires a Mexico en auto")
        
    def test_viaje_en_dron(self):
        input_vehiculo = "dron"
        creador = CreadorTransporte.get_creador(input_vehiculo)
        transporte = creador.get_transporte()
        self.assertEqual(transporte.transportar("Buenos Aires", "Mexico"), "🚁 Volando de Buenos Aires a Mexico")
        
        
        
        
        