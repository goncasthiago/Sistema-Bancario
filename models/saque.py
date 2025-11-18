from models.transacao import Transacao


limite_saques = 5

class Saque(Transacao):
    def __init__(self, valor : float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):

        msg = ""

        excedeu_saldo = self.valor > conta.saldo

        excedeu_limite = self.valor > conta.limite

        excedeu_saques = conta.limite_saques >= limite_saques

        if excedeu_saldo:
            msg = "Operação falhou! Você não possui saldo sufuciente."
            print(msg)
            return False

        elif excedeu_limite:
            msg = "Operação falhou! O valor do saque excedeu o limite."
            print(msg)
            return False

        elif excedeu_saques:
            msg = "Operação falhou! Número de saques foi excedido."
            print(msg)
            return False

        elif self.valor > 0:
            conta.saldo -= self.valor
            conta.extrato += f"Saque: R$ {self.valor: .2f}\n"
            conta.limite_saques += 1
            '''
            transacao = {
                "tipo": "saque",
                "valor": self.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
            '''
            conta.historico.adicionar_transacao(self)
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
