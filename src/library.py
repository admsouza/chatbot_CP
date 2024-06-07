from tabulate import tabulate

def get_search(data):
    collection = {
        'aldir blank, 17199901': '452430000 - OUTRAS TRANSFERÊNCIAS - INTER OFSS - UNIÃO',
        'DCA, MSC, Receita 1 ': '621200000 - RECEITA REALIZADA',
        'DCA, MSC, empenhado, despesa corrente 1': '6.2.2.1.3.01.00 - CREDITO EMPENHADO A LIQUIDAR',
        'DCA, MSC, empenhado, despesa corrente 2': '6.2.2.1.3.02.00 - CREDITO EMPENHADO EM LIQUIDAÇÃO',
        'DCA, MSC, empenhado, despesa corrente 3': '6.2.2.1.3.03.00 - CREDITO EMPENHADO LIQUIDADO A PAGAR',


    }

    data = data.lower()

    # Procurar pelo termo no nome ou no código
    results = [code for key, code in collection.items()
               if data in key.lower() or data in code.lower()]

    if results:
        return results
    else:
        return ['Código não encontrado']

def data_input(user_input):
    data = user_input.strip()
    if data.lower() == 'sair':
        return 'sair', 'Encerrando o chat. Até logo!'

    codigos = get_search(data)
    table = tabulate({"Resultado": codigos}, headers="keys",
                     tablefmt="grid", colalign=("center",))
    response = f'\n{table}\n'

    return 'continuar', f'Termo da busca => {data}{response}'

# Exemplo de uso
estado, resposta = data_input("empenhado")
print(resposta)

estado, resposta = data_input("sair")
print(resposta)
