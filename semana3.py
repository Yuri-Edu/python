agenda = {}

while True:
    print("\n=== Agenda de Contatos ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        agenda[nome] = {'telefone': telefone, 'email': email}
        print(f"Contato {nome} adicionado com sucesso!")
    elif opcao == '2':
        if not agenda:
            print("Nenhum contato na agenda.")
        else:
            for nome, info in agenda.items():
                print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")
    elif opcao == '3':
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in agenda:
            info = agenda[nome]
            print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")
        else:
            print(f"Contato {nome} não encontrado.")
    elif opcao == '4':
        print("Saindo da agenda. Até mais!")
        break 
    else:
        print("Opção inválida. Tente novamente.")
        1