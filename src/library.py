import os
from tabulate import tabulate

def get_search(data):
    collection = {
        'aldir blank, 17199901': '452430000 - OUTRAS TRANSFERÊNCIAS - INTER OFSS - UNIÃO',
        'DCA, MSC, Receita 1': '521110000 - PREVISÃO INICIAL DA RECEITA BRUTA',
        'DCA, MSC, Receita 2': '621200000 -  RECEITA REALIZADA',
        'DCA, MSC, empenhado, despesa corrente 1': '622130100 - CREDITO EMPENHADO A LIQUIDAR',
        'DCA, MSC, empenhado, despesa corrente 2': '622130200 - CREDITO EMPENHADO EM LIQUIDAÇÃO',
        'DCA, MSC, empenhado, despesa corrente 3': '622130300 - CREDITO EMPENHADO LIQUIDADO A PAGAR',

    }

    data = data.lower()

    # Procurar pelo termo no nome ou no código
    results = [code for key, code in collection.items()
               if data in key.lower() or data in code.lower()]

    if results:
        return results
    else:
        return ['Código não encontrado']

def clear_console():
    # Limpar o console com base no sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def data_input(user_input):
    data = user_input.strip()
    if data.lower() == 'sair':
        return 'sair', 'Encerrando o chat. Até logo!'

    clear_console()  # Limpar a impressão anterior

    codigos = get_search(data)
    table = tabulate({"Resultado": codigos}, headers="keys",
                     tablefmt="grid", colalign=("center",))
    response = f'\n{table}\n'

    return 'continuar', f'Termo da busca => {data}{response}'


