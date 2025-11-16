import os
import functools
import csv
from pathlib import Path
from datetime import datetime
import state


ROOT_PATH = Path(__file__).parent
logs = "logs"

try:       

    with open(ROOT_PATH / logs / 'log.csv', 'a', encoding='utf-8', newline='' ) as log:
        escritor = csv.writer(log)





except FileNotFoundError:
    os.mkdir(ROOT_PATH / logs)
    with open(ROOT_PATH / logs / 'log.csv', 'w', encoding='utf-8', newline='' ) as log:
        escritor = csv.writer(log)
        escritor.writerow(['Data', "Função","Argumentos", "Retorno"])


# Decorador para gerar log das funções do Banco
def log_transação(func):
    @functools.wraps(func)
    def cria_log(*args, **kwargs):
        nome_funcao = func.__name__

        # Captura valor se existir em kwargs ou args
        valor = kwargs.get('valor') or (args[1] if len(args) > 1 else None)

        resultado = func(*args, **kwargs)
        with open(ROOT_PATH / logs / 'log.csv', 'a', encoding='utf-8', newline='' ) as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([
                datetime.now(), 
                repr(state.sessao),
                nome_funcao,
                valor, 
                resultado if resultado else ""])
            
        #print(f"Função executada: {nome_funcao}, Data: {datetime.now()}")        
        return resultado

    return cria_log