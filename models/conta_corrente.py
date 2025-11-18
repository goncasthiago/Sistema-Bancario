from models.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super.__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self._saques_realizados = 0
    
    def sacar(self, valor:float):
        
        if valor > self.limite:
            return False
        if self._saques_realizados >= self.limite_saques:
            return False
        
        resultado = super().sacar(valor)
        if resultado:
            self._saques_realizados += 1
        return resultado
    