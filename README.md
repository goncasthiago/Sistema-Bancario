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

## 📊 Diagrama de Fluxo 

[![](https://mermaid.ink/img/pako:eNp1k89um0AQxl9ltWfH8n8cDq0cwJIlu3FLHFUBHzYwtleCXXdZUie2Hybqoaec8gi8WGeBUsVSb_B98_uYmV2ONJIxUJtuEvkz2jGlyZ0bilBMgpko3iIuSSzJUsmtYilbk6urT-Tm6EOWFb8kYZo_sc9nU3-DFvliRFPiBAuZacUUWYDIyUzwiLNkHQqntN3j7b74bYohi2Sy43Gd4poUR3EEV1levCpe562Cj6qJWlXdNNzkUXFFHCk0qyCnhirJkUqB0GBQ5wL1RNmsEefBPUuwIcSWUwIVjMzcuCdHQQwCh-EZuS9eTWF2MkGVPRNPpShPxGnCfcar6IdgytN1sy2fp6XsfVzWXG5ZLMsyr_Sn_9vW1KS4sJcZ13X3rrcMvgEO8IICWsU7eiYMjepjDeizqIb8ydd_kM9-5GZHKF4A3gGb1NWBeN_vAu_AH3GyWkYExQsEZ5G5LsXbFRIiAmUGrS8QMihXZ0FbdKt4TG2tcmjRFFTKzCs9hoKQkOodpBBSGx9j2LA80SENxRmxPRMPUqZ_SSXz7Y7aG5Zk-JbvY6bB5cxc4KYERAzKkbnQ1B50x2UGtY_0QO1xvz3uD7qW1bF64-trq0Wfqd0ftTuj3mA4tAa97mDY7Y3OLfpSfrTTHlvDFoUY96wW1c9U_lPnP46sGoE?type=png)](https://mermaid.live/edit#pako:eNp1k89um0AQxl9ltWfH8n8cDq0cwJIlu3FLHFUBHzYwtleCXXdZUie2Hybqoaec8gi8WGeBUsVSb_B98_uYmV2ONJIxUJtuEvkz2jGlyZ0bilBMgpko3iIuSSzJUsmtYilbk6urT-Tm6EOWFb8kYZo_sc9nU3-DFvliRFPiBAuZacUUWYDIyUzwiLNkHQqntN3j7b74bYohi2Sy43Gd4poUR3EEV1levCpe562Cj6qJWlXdNNzkUXFFHCk0qyCnhirJkUqB0GBQ5wL1RNmsEefBPUuwIcSWUwIVjMzcuCdHQQwCh-EZuS9eTWF2MkGVPRNPpShPxGnCfcar6IdgytN1sy2fp6XsfVzWXG5ZLMsyr_Sn_9vW1KS4sJcZ13X3rrcMvgEO8IICWsU7eiYMjepjDeizqIb8ydd_kM9-5GZHKF4A3gGb1NWBeN_vAu_AH3GyWkYExQsEZ5G5LsXbFRIiAmUGrS8QMihXZ0FbdKt4TG2tcmjRFFTKzCs9hoKQkOodpBBSGx9j2LA80SENxRmxPRMPUqZ_SSXz7Y7aG5Zk-JbvY6bB5cxc4KYERAzKkbnQ1B50x2UGtY_0QO1xvz3uD7qW1bF64-trq0Wfqd0ftTuj3mA4tAa97mDY7Y3OLfpSfrTTHlvDFoUY96wW1c9U_lPnP46sGoE)



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
