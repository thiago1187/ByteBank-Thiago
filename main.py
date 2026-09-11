import contas
import operacoes


def menu_conta(conta):
    while True:
        print()
        print(f"=== Conta {conta['numero']} - {conta['nome']} ===")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Voltar")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            contas.mostrar_saldo(conta)
        elif opcao == "2":
            operacoes.depositar(conta)
        elif opcao == "3":
            operacoes.sacar(conta)
        elif opcao == "4":
            break
        else:
            print("Opcao invalida.")


def menu_inicial():
    while True:
        print()
        print("=== ByteBank ===")
        print("1 - Cadastrar conta")
        print("2 - Acessar conta")
        print("3 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            contas.cadastrar_conta()
        elif opcao == "2":
            conta = contas.acessar_conta()
            if conta is None:
                print("Conta nao encontrada.")
            else:
                menu_conta(conta)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


menu_inicial()
