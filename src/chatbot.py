from library import data_input


def main():
    print("Bem-vindo ao chatbot!")

    while True:
        user_input = input("Digte sua busca ou sair para encerrar ")
        status, response = data_input(user_input)
        print(response)

        if status == 'sair':
            break

    print("Chat encerrado.")


if __name__ == '__main__':
    main()
