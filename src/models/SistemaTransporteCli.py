from src.models.SistemaTransporteAbs import SistemaTransporteAbs

class SistemaTransporteCli(SistemaTransporteAbs):
    def __init__(self):
        super().__init__()
        
    
    def conseguir_input_vehiculo(self):
        self.vehiculo = input("Ingrese el tipo de transporte (auto/dron):")
    
    def conseguir_input_origen_destino(self):
        self.origen = input("Ingrese el origen: ")
        self.destino = input("Ingrese el destino: ")
    
    