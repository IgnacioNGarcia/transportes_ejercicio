from src.models.SistemaTransporteAbs import SistemaTransporteAbs
import argparse

class SistemaTransporteScript(SistemaTransporteAbs):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser(description="Script para viajar en auto o dron")
        self.parser.add_argument("--vehiculo", required=True, help="Tipo de vehiculo (auto/dron)")
        self.parser.add_argument("--origen", required=True, help="Ciudad de origen")
        self.parser.add_argument("--destino", required=True, help="Ciudad de destino")
        
        
    def conseguir_input_vehiculo(self):
        args = self.parser.parse_args()
        self.vehiculo = args.vehiculo
        
    def conseguir_input_origen_destino(self):
        args = self.parser.parse_args()
        self.origen = args.origen
        self.destino = args.destino
        
        
        