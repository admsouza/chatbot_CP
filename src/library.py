from tabulate import tabulate


def get_search(data):

    collection = {
        'receita realizada': '1111111111 - receita realizada',


        'receita prevista ': '222222222222 - receita prevista',
    }

    data = data.lower()

    results = [code for key, code in collection.items()
               if data in key or data in code]

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
