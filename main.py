import contas


def depositar(conta):
    try:
        valor = float(input("Valor do deposito: R$ "))
    except ValueError:
        print("Valor invalido.")
        return
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return
    conta["saldo"] += valor
    print(f"Deposito de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


def sacar(conta):
    try:
        valor = float(input("Valor do saque: R$ "))
    except ValueError:
        print("Valor invalido.")
        return
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    conta["saldo"] -= valor
    print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


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
            depositar(conta)
        elif opcao == "3":
            sacar(conta)
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
