from models.saque import Saque
from models.deposito import Deposito
from models.historico import Historico
class Conta:

    _limite = 500
    _limite_saques = 5

    def __init__(self, cliente, numero, agencia = "0001"):
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._saldo = 0.0
        self._historico = Historico()
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero )
    
    def sacar(self, valor: float):
        transacao = Saque(valor)
        return transacao.registrar(self)
    
    def depositoar(self, valor: float):
        transacao = Deposito(valor)
        return transacao.registrar(self)
