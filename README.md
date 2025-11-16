🏦 Sistema Bancário em Python (CLI) — Versão Estruturada com Decoradores, Geradores e Iteradores

Este projeto implementa um Sistema Bancário completo via linha de comando, utilizando Python e boas práticas de organização de código.
A versão atual conta com:

Decorador de Log para rastrear operações sensíveis

Iterador de Contas (ContaIterador) para percorrer contas de forma padronizada

Gerador de Transações (Historico.gerar_relatorio) para relatórios eficientes

Separação em múltiplos módulos

Simulação de operações bancárias reais: criação de usuários, contas, depósitos, saques e extratos

Ele serve para estudo de Python intermediário/avançado, boas práticas estruturais e conceitos como funções de ordem superior, iteradores manuais e geradores.




📌 Funcionalidades Principais (Versão Técnica)
🧩 Arquitetura Modular

Separação do sistema em múltiplos módulos independentes (```historico.py```, ```conta_iterador.py```, ```decoradores.py```, etc.).

Cada módulo encapsula uma responsabilidade única:

- Iterador personalizado para percorrer contas

- Gerador de transações para processamento lazy

- Decorador de auditoria acoplado a funções críticas

👤 Gerenciamento de Usuários

Estrutura de dados baseada em ```dict```, usando o CPF como chave hash primária.

Implementação de CRUD básico para usuários, mantendo isolamento entre camadas.

🏦 Administração de Contas Correntes

Associação entre usuários e múltiplas contas (mapeamento 1:N).

Normalização do número de contas via função geradora de IDs no padrão ```000001-1```.

Implementação de um iterador customizado (```ContaIterador```):

Suporte a protocolo iterator (```__iter__```/```__next__```)

Flatten de contas para iteração linear

Entrega de dados formatados para inspeção ou exportação

💰 Operações Bancárias

- Fluxo de transações estruturado com:

Sanitização e validação de entrada

Atualização transacional do estado da conta

Registro simultâneo em histórico e log

- Regras de negócio integradas:

limite por saque

limite diário

número máximo de operações

validação de saldo

📜 Histórico de Transações (Gerador)

Histórico baseado em **generator function**, permitindo:

iteração lazy

redução de uso de memória

filtros dinâmicos de tipos de operação (saque, deposito)

Adequado para extração de relatórios extensos sem custo adicional de alocação.

🧾 Auditoria via Decoradores (Log Automático)

Decorador **log_transação** aplicado a funções sensíveis:

registra timestamp, método, argumentos e contexto operacional

permite extensão futura para persistência em arquivo, S3 ou banco de dados


🔑 Gerenciamento de Autenticação e Sessão

Sessão controlada via estrutura dedicada (sessao) contendo:

- CPF autenticado

- conta ativa

- status de login

- Isolamento entre contexto global e contexto da operação.

🧭 CLI para Navegação

Interface por menu que funciona como controlador de fluxo (controller).

Rotinas distintas para:

onboarding de usuários

login

operações autenticadas

Estrutura compatível com futura migração para frameworks (Flask/FastAPI).


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

🧾 Decorador de Log (log_decorador)

Agora aparece como um nó independente no fluxo.
Cada operação crítica (depósito, saque, extrato) passa por ele antes de alterar o estado da conta.

intercepta a chamada

grava timestamp

persiste o log na estrutura do usuário

devolve o fluxo à função original

🔁 Iterador de Contas (ContaIterador)

Incluído como um bloco próprio:

recebe o dicionário completo de contas

transforma em uma lista linear

responde via __next__() a cada iteração

quando acabar, levanta StopIteration

🔄 Gerador de Histórico (Historico.gerar_relatorio)

Mostrado como um nó do tipo "função geradora":

produz transações sob demanda

reduz memória usada

suporta filtros por tipo de transação



## 📌 Regras Importantes do Sistema

Cada CPF pode possuir **uma** ou **mais** contas.

O limite diário de saques é definido por **LIMITE_SAQUES**.

O limite máximo por saque é configurado na chave **limite** dentro da conta.

O extrato é registrado como **string** (modelo simples de auditoria).


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
