contas = []


def ler_valor(mensagem):
    try:
        valor = float(input(mensagem))
    except ValueError:
        print("Valor invalido.")
        return None
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return None
    return valor


def buscar_por_chave(chave):
    for conta in contas:
        if conta["chave_pix"] == chave:
            return conta
    return None


def buscar_por_numero(numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None


def cadastrar_conta():
    nome = input("Nome do titular: ").strip()
    chave_pix = input("Chave pix: ").strip()
    if not nome or not chave_pix:
        print("Nome e chave pix nao podem ficar em branco.")
        return
    if buscar_por_chave(chave_pix) is not None:
        print("Ja existe uma conta com essa chave pix.")
        return
    contas.append({
        "numero": len(contas) + 1, "nome": nome, "chave_pix": chave_pix,
        "saldo": 0.0, "extrato": [], "boletos": [],
    })
    print(f"Conta {len(contas)} criada para {nome}.")


def acessar_conta():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("Contas cadastradas:")
    for conta in contas:
        print(f"{conta['numero']} - {conta['nome']}")
    try:
        numero = int(input("Numero da conta: "))
    except ValueError:
        print("Numero invalido.")
        return None
    return buscar_por_numero(numero)


def mostrar_saldo(conta):
    print(f"{conta['nome']}: R$ {conta['saldo']:.2f}")


def registrar(conta, tipo, valor, destino):
    conta["extrato"].append({"tipo": tipo, "valor": valor, "destino": destino})


def depositar(conta):
    valor = ler_valor("Valor do deposito: R$ ")
    if valor is None:
        return
    conta["saldo"] += valor
    registrar(conta, "deposito", valor, None)
    print(f"Deposito de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


def sacar(conta):
    valor = ler_valor("Valor do saque: R$ ")
    if valor is None:
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    conta["saldo"] -= valor
    registrar(conta, "saque", valor, None)
    print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


def pix(conta):
    destino = buscar_por_chave(input("Chave pix de destino: ").strip())
    if destino is None:
        print("Chave pix nao encontrada.")
        return
    if destino is conta:
        print("Nao da para transferir para a propria conta.")
        return
    valor = ler_valor("Valor do pix: R$ ")
    if valor is None:
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    conta["saldo"] -= valor
    destino["saldo"] += valor
    registrar(conta, "pix", valor, destino["chave_pix"])
    print(f"Pix de R$ {valor:.2f} enviado para {destino['nome']}. Saldo: R$ {conta['saldo']:.2f}")


def mostrar_extrato(conta):
    if not conta["extrato"]:
        print("Nenhuma transacao registrada.")
        return
    print("Extrato (mais recente primeiro):")
    for transacao in reversed(conta["extrato"]):
        print(f"{transacao['tipo']} - R$ {transacao['valor']:.2f}")


def estornar(conta):
    if not conta["extrato"]:
        print("Nao ha transacao para estornar.")
        return
    transacao = conta["extrato"].pop()
    tipo, valor = transacao["tipo"], transacao["valor"]
    if tipo == "deposito":
        conta["saldo"] -= valor
    else:
        conta["saldo"] += valor
    if tipo == "pix":
        destino = buscar_por_chave(transacao["destino"])
        if destino is not None:
            destino["saldo"] -= valor
    print(f"Estorno de {tipo} no valor de R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")


def agendar_boleto(conta):
    descricao = input("Descricao do boleto: ").strip()
    if not descricao:
        print("A descricao nao pode ficar em branco.")
        return
    valor = ler_valor("Valor do boleto: R$ ")
    if valor is None:
        return
    conta["boletos"].append({"descricao": descricao, "valor": valor})
    print(f"Boleto '{descricao}' de R$ {valor:.2f} agendado.")


def ver_fila(conta):
    if not conta["boletos"]:
        print("Nenhum boleto na fila.")
        return
    print("Fila de boletos (proximo a pagar primeiro):")
    for boleto in conta["boletos"]:
        print(f"{boleto['descricao']} - R$ {boleto['valor']:.2f}")


def liquidar_pagamentos(conta):
    if not conta["boletos"]:
        print("Nenhum boleto na fila.")
        return
    while conta["boletos"]:
        proximo = conta["boletos"][0]
        if proximo["valor"] > conta["saldo"]:
            print(f"Sem saldo para o boleto '{proximo['descricao']}' de R$ {proximo['valor']:.2f}.")
            break
        conta["boletos"].pop(0)
        conta["saldo"] -= proximo["valor"]
        registrar(conta, "boleto", proximo["valor"], None)
        print(f"Boleto '{proximo['descricao']}' pago. Saldo: R$ {conta['saldo']:.2f}")


def menu_conta(conta):
    while True:
        print(f"\n=== Conta {conta['numero']} - {conta['nome']} ===")
        print("1 - Consultar saldo\n2 - Depositar\n3 - Sacar\n4 - Pix\n"
              "5 - Ver extrato\n6 - Estornar ultima transacao\n7 - Agendar boleto\n"
              "8 - Ver fila de boletos\n9 - Liquidar pagamentos\n10 - Voltar")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            mostrar_saldo(conta)
        elif opcao == "2":
            depositar(conta)
        elif opcao == "3":
            sacar(conta)
        elif opcao == "4":
            pix(conta)
        elif opcao == "5":
            mostrar_extrato(conta)
        elif opcao == "6":
            estornar(conta)
        elif opcao == "7":
            agendar_boleto(conta)
        elif opcao == "8":
            ver_fila(conta)
        elif opcao == "9":
            liquidar_pagamentos(conta)
        elif opcao == "10":
            break
        else:
            print("Opcao invalida.")


def menu_inicial():
    while True:
        print("\n=== ByteBank ===")
        print("1 - Cadastrar conta\n2 - Acessar conta\n3 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            cadastrar_conta()
        elif opcao == "2":
            conta = acessar_conta()
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
