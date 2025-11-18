from abc import ABC, abstractmethod

class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta)-> bool:
        pass

    @property
    @abstractmethod
    def valor(self) -> float:
        pass
