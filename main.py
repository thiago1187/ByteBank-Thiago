def menu_inicial():
    while True:
        print()
        print("=== ByteBank ===")
        print("1 - Cadastrar conta")
        print("2 - Acessar conta")
        print("3 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            print("Cadastro de conta ainda nao implementado.")
        elif opcao == "2":
            print("Acesso a conta ainda nao implementado.")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


menu_inicial()
