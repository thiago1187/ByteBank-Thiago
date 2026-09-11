contas = []


def cadastrar_conta():
    nome = input("Nome do titular: ").strip()
    chave_pix = input("Chave pix: ").strip()
    if not nome or not chave_pix:
        print("Nome e chave pix nao podem ficar em branco.")
        return
    if buscar_por_chave(chave_pix) is not None:
        print("Ja existe uma conta com essa chave pix.")
        return
    numero = len(contas) + 1
    conta = {
        "numero": numero,
        "nome": nome,
        "chave_pix": chave_pix,
        "saldo": 0.0,
        "extrato": [],
        "boletos": [],
    }
    contas.append(conta)
    print(f"Conta {numero} criada para {nome}.")


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
    try:
        valor = float(input("Valor do deposito: R$ "))
    except ValueError:
        print("Valor invalido.")
        return
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return
    conta["saldo"] += valor
    registrar(conta, "deposito", valor, None)
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
    registrar(conta, "saque", valor, None)
    print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


def pix(conta):
    chave_destino = input("Chave pix de destino: ").strip()
    destino = buscar_por_chave(chave_destino)
    if destino is None:
        print("Chave pix nao encontrada.")
        return
    if destino is conta:
        print("Nao da para transferir para a propria conta.")
        return
    try:
        valor = float(input("Valor do pix: R$ "))
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
    destino["saldo"] += valor
    registrar(conta, "pix", valor, destino["chave_pix"])
    print(f"Pix de R$ {valor:.2f} enviado para {destino['nome']}. Saldo: R$ {conta['saldo']:.2f}")


def mostrar_extrato(conta):
    lista = conta["extrato"]
    if not lista:
        print("Nenhuma transacao registrada.")
        return
    print("Extrato (mais recente primeiro):")
    for i in range(len(lista) - 1, -1, -1):
        transacao = lista[i]
        print(f"{transacao['tipo']} - R$ {transacao['valor']:.2f}")


def estornar(conta):
    if not conta["extrato"]:
        print("Nao ha transacao para estornar.")
        return
    transacao = conta["extrato"].pop()
    tipo = transacao["tipo"]
    valor = transacao["valor"]
    if tipo == "deposito":
        conta["saldo"] -= valor
    elif tipo == "saque":
        conta["saldo"] += valor
    elif tipo == "boleto":
        conta["saldo"] += valor
    elif tipo == "pix":
        conta["saldo"] += valor
        destino = buscar_por_chave(transacao["destino"])
        if destino is not None:
            destino["saldo"] -= valor
    print(f"Estorno de {tipo} no valor de R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")


def agendar_boleto(conta):
    descricao = input("Descricao do boleto: ").strip()
    if not descricao:
        print("A descricao nao pode ficar em branco.")
        return
    try:
        valor = float(input("Valor do boleto: R$ "))
    except ValueError:
        print("Valor invalido.")
        return
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return
    conta["boletos"].append({"descricao": descricao, "valor": valor})
    print(f"Boleto '{descricao}' de R$ {valor:.2f} agendado.")


def ver_fila(conta):
    fila = conta["boletos"]
    if not fila:
        print("Nenhum boleto na fila.")
        return
    print("Fila de boletos (proximo a pagar primeiro):")
    for boleto in fila:
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
        boleto = conta["boletos"].pop(0)
        conta["saldo"] -= boleto["valor"]
        registrar(conta, "boleto", boleto["valor"], None)
        print(f"Boleto '{boleto['descricao']}' pago. Saldo: R$ {conta['saldo']:.2f}")


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
        print()
        print("=== ByteBank ===")
        print("1 - Cadastrar conta")
        print("2 - Acessar conta")
        print("3 - Sair")
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
