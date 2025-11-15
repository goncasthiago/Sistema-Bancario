# 🏦 Sistema Bancário em Python (CLI)

Este projeto implementa um Sistema Bancário em modo texto utilizando Python.
O objetivo é simular operações essenciais de um banco, como criação de usuários, abertura de contas, depósitos, saques e emissão de extratos, empregando boas práticas de programação estruturada.




## 📌 Funcionalidades Principais

- Criação de Usuários
Cadastro de clientes utilizando CPF como chave única.

- Abertura de Conta Corrente
Geração automática de número de conta no formato 000001-1.

- Login e Gerenciamento de Sessão
Controle de estado para identificar o usuário e a conta ativa.

- Depósitos
Atualização de saldo e registro no extrato.

- Saques
Validação de:

saldo insuficiente

limite máximo por operação

limite diário de saques

valor inválido

- Extrato Bancário
Exibição das movimentações registradas e saldo atual.

- Menus Interativos
Interfaces distintas para usuários autenticados e não autenticados.

## 📊 Diagrama de Fluxo (Flowchart)

flowchart TD

A[Início do Programa] --> B{Sessão ativa?}

B -- Não --> C[Mostrar Menu Inicial]
C --> D{Opção escolhida?}

D -- Criar Usuário --> CU[Criar Usuário]
CU --> B

D -- Abrir Conta --> CC[Criar Conta Corrente]
CC --> B

D -- Entrar --> L[Validar CPF e Conta]
L -->|Credenciais Válidas| B
L -->|Inválido| C

D -- Sair --> Z[Fim]

B -- Sim --> E[Mostrar Menu Logado]

E --> F{Opção escolhida?}

F -- Depositar --> DEP[Realizar Depósito]
DEP --> E

F -- Sacar --> SAQ[Realizar Saque]
SAQ --> E

F -- Extrato --> EXT[Exibir Extrato]
EXT --> E

F -- Logout --> OUT[Encerrar Sessão]
OUT --> B



## 🚀 Como Executar

Certifique-se de ter o Python 3 instalado.

Clone o repositório:

```
git clone https://github.com/seuusuario/sistema-bancario-python.git
cd sistema-bancario-python
```


Execute o script:

```
python sistema_bancario.py
```

## 🛠️ Tecnologias Utilizadas

Python 3.x

Entrada e saída padrão (```input```, ```print```)

Estruturas de dados nativas (```dict```, ```list```, ```str```)

Controle de fluxo com loops e condicionais

## 🧱 Arquitetura do Sistema

O sistema é implementado em um único arquivo, organizado em:

1. Funções de Operações Bancárias

```saque()```

```deposito()```

```extrato_conta()```

2. Funções de Gerenciamento

```criar_usuario()```

```criar_conta_corrente()```

```proximo_numero_disponivel()```

```sessao_ativa()```

3. Estruturas de Dados

```usuarios``` → base de clientes

```conta_corrente``` → contas associadas a cada CPF

```sessao``` → controle de autenticação

4. Interface de Navegação

```login``` → menu inicial

```menu``` → menu autenticado
## 📂 Fluxo Geral do Programa

1. Usuário acessa o menu inicial

2. Pode criar um usuário ou abrir uma conta

3. Realiza login informando CPF e conta

4. Acessa o menu bancário:

- Depósito

- Saque

- Extrato

- Logout

O programa permanece em execução até o usuário encerrar


## 📌 Regras Importantes do Sistema

Cada CPF pode possuir **uma** ou **mais** contas.

O limite diário de saques é definido por **LIMITE_SAQUES**.

O limite máximo por saque é configurado na chave **limite** dentro da conta.

O extrato é registrado como **string** (modelo simples de auditoria).

## ⚠️ Limitações / Próximos Passos

Implementar senha e um login mais robusto

Salvar dados em arquivo ou banco de dados real

Implementar gerenciamento de múltiplos usuários simultâneos

Adicionar validações mais robustas de CPF

Criar testes automatizados

Migrar lógica para programação orientada a objetos (POO)

## 🤝 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para abrir Issues ou enviar Pull Requests.
## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de thiagodebia@gmail.com


## Autores

- [@goncashiago](https://www.github.com/goncasthiago)
