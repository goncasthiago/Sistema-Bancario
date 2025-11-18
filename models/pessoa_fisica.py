from datetime import date
from models.cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self,/,*, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
