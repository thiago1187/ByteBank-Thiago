import contas
import operacoes
import extrato
import boletos


def menu_conta(conta):
    while True:
        print()
        print(f"=== Conta {conta['numero']} - {conta['nome']} ===")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Pix")
        print("5 - Ver extrato")
        print("6 - Estornar ultima transacao")
        print("7 - Agendar boleto")
        print("8 - Ver fila de boletos")
        print("9 - Liquidar pagamentos")
        print("10 - Voltar")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            contas.mostrar_saldo(conta)
        elif opcao == "2":
            operacoes.depositar(conta)
        elif opcao == "3":
            operacoes.sacar(conta)
        elif opcao == "4":
            operacoes.pix(conta)
        elif opcao == "5":
            extrato.mostrar_extrato(conta)
        elif opcao == "6":
            extrato.estornar(conta)
        elif opcao == "7":
            boletos.agendar_boleto(conta)
        elif opcao == "8":
            boletos.ver_fila(conta)
        elif opcao == "9":
            boletos.liquidar_pagamentos(conta)
        elif opcao == "10":
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
