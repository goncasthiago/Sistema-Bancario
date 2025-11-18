from models.transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):

        if self.valor > 0:
            conta.saldo += self.valor
            conta.extrato += f"Deposito: R$ {self.valor: .2f}\n"
            conta.historico.adicionar_transacao(self)
            print(f"Depósito de {self.valor} efetuado com sucesso!")
            return True
        else:
            print("""Operação falhou! O valor informado é inválido.
        Tente novamente!""")
            return False

    
