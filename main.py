saldo = 0.0


def consultar_saldo():
    print(f"Saldo: R$ {saldo:.2f}")


def depositar():
    global saldo
    valor = float(input("Valor do deposito: R$ "))
    saldo += valor
    print(f"Deposito de R$ {valor:.2f} realizado. Saldo: R$ {saldo:.2f}")


def sacar():
    global saldo
    valor = float(input("Valor do saque: R$ "))
    saldo -= valor
    print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {saldo:.2f}")


def menu_inicial():
    while True:
        print()
        print("=== ByteBank ===")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


menu_inicial()
