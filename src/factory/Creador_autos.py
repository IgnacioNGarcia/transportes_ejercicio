from src.factory.Creador import CreadorTransporte
from src.models.Auto import Auto
from src.models.Transporte import Transporte

class CreadorAutos(CreadorTransporte):
    
    def crear_transporte(self) -> Transporte:
        return Auto()
