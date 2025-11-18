from datetime import datetime

import state
from conta_iterador import ContaIterador
from gerador import log_transação
from historico import Historico

historico = Historico()

# Funções diretamente ligadas a tarefas do banco


@log_transação
def saque(*, conta, valor, limite_saques):

    msg = ""

    excedeu_saldo = valor > conta["saldo"]

    excedeu_limite = valor > conta["limite"]

    excedeu_saques = conta["numero_saques"] >= limite_saques

    if excedeu_saldo:
        msg = "Operação falhou! Você não possui saldo sufuciente."
        print(msg)
        return msg

    elif excedeu_limite:
        msg = "Operação falhou! O valor do saque excedeu o limite."
        print(msg)
        return msg

    elif excedeu_saques:
        msg = "Operação falhou! Número de saques foi excedido."
        print(msg)
        return msg

    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor: .2f}\n"
        conta["numero_saques"] += 1
        transacao = {
            "tipo": "saque",
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }

        historico.adicionar_transacao(transacao)
        return transacao
    else:
        msg = "Operação falhou! O valor informado é inválido."
        print(msg)
        return msg


@log_transação
def deposito(conta, valor):
    conta = sessao_ativa()

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Deposito: R$ {valor: .2f}\n"
        transacao = {
            "tipo": "deposito",
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }
        historico.adicionar_transacao(transacao)
        print(f"Depósito de {valor} efetuado com sucesso!")
        return transacao
    else:
        msg = """Operação falhou! O valor informado é inválido.
Tente novamente!"""
        print(msg)
        return msg


@log_transação
def extrato_conta(conta):

    print("\n#############EXTRATO#############")
    print(
        "Não foram realizadas movimentações."
        if not conta["extrato"]
        else conta["extrato"]
    )
    print(f"\nSaldo: R$ {conta['saldo']: .2f}")
    print("#################################")

    transacoes = []
    for transacao in historico.gerar_relatorio(tipo_transacao="saque"):
        transacoes.append(transacao)

    return transacoes


@log_transação
def criar_usuario(nome, data_nascimento, cpf, endereco):
    if cpf not in usuarios:
        usuarios[cpf] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }
        return usuarios[cpf]

    else:
        msg = "Já existe um usuário com esse CPF!"
        print(msg)
        return msg


@log_transação
def criar_conta_corrente(agencia, numero_conta, usuario):
    if usuario in usuarios:
        # Garante que o usuario exista em conta corrente
        conta_corrente.setdefault(usuario, {})

        # Cria a nova conta corrente
        conta_corrente[usuario][numero_conta] = {
            "agencia": agencia,
            "saldo": 0,
            "extrato": "",
            "limite": 500,
            "numero_saques": 0,
        }

        return conta_corrente[usuario][numero_conta]


# Funções administrativas para que todo código funcione corretamente


def gerador_relatorios(extrato: str):
    for linha in extrato:
        yield linha


def proximo_numero_disponivel():
    """Retorna o proximo numero disponível para Conta Corrente"""
    contas = []

    # Busca todos os CPFs nas contas atuais
    cpfs = [cpf for cpf in conta_corrente.keys()]

    # Busca os numeros utilizados - cada CPF pode ter mais de uma conta
    for cpf in cpfs:
        contas.extend([int(conta.split("-")[0]) for conta in conta_corrente[cpf]])
    # Pega o valor mais alto e soma 1
    numero_conta = str(max(contas) + 1).zfill(6) + "-" + "1"
    return numero_conta


def listar_contas():
    """Retorna uma lista com todas as contas corrente cadastradas no Banco"""

    for conta in ContaIterador(conta_corrente):
        print(conta)


def sessao_ativa():
    """Retorna a conta corrente do usuário logado"""
    return conta_corrente[state.sessao["cpf"]][state.sessao["conta_corrente"]]


def mensagem_controle():
    input("\n\nPressione [Enter] para continuar...")


# Tela inicial


login = """

##################################
##      Sistema Bancário        ##
##                              ##
##    Escolha uma das opções    ##
##      para prosseguir:        ##
##                              ##
##      [e] Entrar              ##
##      [c] Criar Usuario       ##
##      [ac] Abrir Conta        ##
##      [lc] Listar Contas      ##
##      [q] Sair                ##
##                              ##
##                              ##
##################################

=> """

# Tela do cliente com sessao ativa


menu = """

##################################
##      Sistema Bancário        ##
##                              ##
##    Escolha uma das opções    ##
##      para prosseguir:        ##
##                              ##
##      [d] Depositar           ##
##      [s] Sacar               ##
##      [e] Extrato             ##
##      [q] Sair                ##
##                              ##
##                              ##
##################################


=> """

# Variaveis Globais


LIMITE_SAQUES = 2

usuarios = {
    "11111111111": {
        "nome": "João Silva",
        "data_nascimento": "10/01/1990",
        "endereco": "Rua A, 123 - Cidade X",
    },
    "11111111112": {
        "nome": "Maria Silva",
        "data_nascimento": "11/01/1990",
        "endereco": "Rua A, 123 - Cidade X",
    },
}

conta_corrente = {
    "11111111111": {
        "123457-7": {
            "agencia": "0001",
            "saldo": 0,
            "extrato": "",
            "limite": 500,
            "numero_saques": 0,
        },
        "123456-7": {
            "agencia": "0001",
            "saldo": 0,
            "extrato": "",
            "limite": 500,
            "numero_saques": 0,
        },
    },
    "11111111112": {
        "123458-7": {
            "agencia": "0001",
            "saldo": 0,
            "extrato": "",
            "limite": 500,
            "numero_saques": 0,
        }
    },
}


while True:
    if not state.sessao["logado"]:

        opcao = input(login)
        if opcao == "c":
            print("Informe os seguintes dados para criarmos seu usuário: ")
            nome = input("Informe seu nome completo: ")
            data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe seu CPF (somente números): ")
            endereco = input(
                "Informe seu endereço (logradouro, número - bairro - cidade/sigla estado): "
            )

            criar_usuario(nome, data_nascimento, cpf, endereco)
            print("\n\nUsuário criado com sucesso!")
            mensagem_controle()

        elif opcao == "ac":
            usuario = input("Informe seu CPF (somente números): ")

            if usuario in usuarios:
                # Busca ultimo numero de conta disponível para criação de próxima conta
                numero_conta = proximo_numero_disponivel()
                agencia = "0001"  # Valor fixo

                criar_conta_corrente(agencia, numero_conta, usuario)

                # Retorno para o cliente!
                print("\n\nConta criada com sucesso!")
                print(f"Agência: {conta_corrente[usuario][numero_conta]['agencia']}")
                print(f"Número da Conta: {numero_conta}")
                mensagem_controle()

            else:
                print(
                    "Usuário não encontrado, por favor crie um usuário antes de abrir uma conta."
                )
                mensagem_controle()

        elif opcao == "e":
            cpf = str(input("Informe seu CPF (somente números): "))
            numero_conta = str(input("Informe seu numero da conta: "))

            # Iniciar a Sessao do cliente
            if cpf in conta_corrente and numero_conta in conta_corrente[cpf]:
                state.sessao = {
                    "logado": True,
                    "cpf": cpf,
                    "conta_corrente": numero_conta,
                }

            else:
                print("\n\nNão encontramos seu cadastro!\n\n")
                mensagem_controle()

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )
            mensagem_controle()

    else:
        # Cliente logado

        # Configura a conta ativa do cliente
        conta = sessao_ativa()

        opcao = input(menu)

        # Depositar
        if opcao == "d":

            valor = float(input("Informe o valor do depósito: "))

            # Efetua o deposito na conta corrente
            deposito(conta, valor)
            mensagem_controle()

        # Sacar
        elif opcao == "s":

            valor = float(input("Informe o valor do saque: "))

            # Efetua o saque na conta corrente
            saque(conta=conta, valor=valor, limite_saques=LIMITE_SAQUES)

            mensagem_controle()

        # Extrato
        elif opcao == "e":

            # Mostra o extrato na tela se existir movimentações na conta.
            extrato_conta(conta)
            mensagem_controle()

        elif opcao == "q":

            # Apaga a sessao do cliente
            state.sessao = {"logado": False, "cpf": "", "conta_corrente": ""}

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )
            mensagem_controle()
