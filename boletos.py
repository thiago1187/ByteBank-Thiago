import extrato


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
        extrato.registrar(conta, "boleto", boleto["valor"], None)
        print(f"Boleto '{boleto['descricao']}' pago. Saldo: R$ {conta['saldo']:.2f}")
