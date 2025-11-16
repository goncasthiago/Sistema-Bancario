class ContaIterador():
    def __init__(self, contas):
        self.dados_bancarios = contas
        self.contas = self._contas_organizadas(contas)
        self.contador = 0    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            return f"""
            -----------------------------
            
            CPF Cliente: {conta[0]} 
            Conta Corrente: {conta[1]} 
            Dados da conta: 

            - Agência: {conta[2]['agencia']}
            - Saldo: {conta[2]['saldo']}
            - Extrato: {conta[2]['extrato']}
            - Limite: {conta[2]['limite']}
            - Número de Saques: {conta[2]['numero_saques']}
            """
        except IndexError:
            print("""
            -----------------------------""")
            raise StopIteration

    def _contas_organizadas(self, dados_bancarios):
        contas = []
        cpfs = [cpf for cpf in dados_bancarios.keys()]
        for cpf in cpfs:
            contas.extend([(cpf, conta, dados_bancarios[cpf][conta] ) for conta in dados_bancarios[cpf]])
        
        return contas   