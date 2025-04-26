from src.models.Transporte import Transporte

class Auto(Transporte):
    
    def __init__(self):
        super().__init__()
    
    def transportar(self, origen :str, destino :str):
        return f"🚗 Transportando de {origen} a {destino} en auto"
        