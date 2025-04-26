from abc import ABC, abstractmethod

class Transporte(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def transportar(self, origen :str, destino :str):
        pass