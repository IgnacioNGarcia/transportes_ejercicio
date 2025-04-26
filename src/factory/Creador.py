from abc import ABC, abstractmethod
from src.models.Transporte import Transporte

class CreadorTransporte(ABC):
    
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        pass
        
    def get_transporte(self) -> Transporte:
        return self.crear_transporte()
        
    @staticmethod
    def get_creador(tipo: str) -> 'CreadorTransporte':
        if tipo.lower() == "auto":
            from src.factory.Creador_autos import CreadorAutos
            return CreadorAutos()
        elif tipo.lower() == "dron":
            from src.factory.Creador_drones import CreadorDrones
            return CreadorDrones()
        else:
            raise ValueError("Opción no válida")