from src.models.Transporte import Transporte

class Dron(Transporte):
    
    def __init__(self):
        super().__init__()
    
    def transportar(self, origen :str, destino :str):
        return f"🚁 Volando de {origen} a {destino}"
        
        
        