from src.factory.Creador import CreadorTransporte
from src.models.Dron import Dron
from src.models.Transporte import Transporte

class CreadorDrones(CreadorTransporte):
    
    def crear_transporte(self) -> Transporte:
        return Dron()
