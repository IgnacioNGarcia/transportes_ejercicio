from abc import ABC, abstractmethod

class SistemaTransporteAbs(ABC):
    
    def __init__(self):
        self.vehiculo = None
        self.origen = None
        self.destino = None
    
    @abstractmethod
    def conseguir_input_vehiculo(self):
        pass

    @abstractmethod
    def conseguir_input_origen_destino(self):
        pass
    
    
    
