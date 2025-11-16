from datetime import datetime

class Historico():
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
    
    def gerar_relatorio(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao != None and (tipo_transacao == "saque" or tipo_transacao == "deposito"):
                yield transacao
            else:
                yield transacao
            