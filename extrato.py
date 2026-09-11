import contas


def registrar(conta, tipo, valor, destino):
    conta["extrato"].append({"tipo": tipo, "valor": valor, "destino": destino})


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
        destino = contas.buscar_por_chave(transacao["destino"])
        if destino is not None:
            destino["saldo"] -= valor
    print(f"Estorno de {tipo} no valor de R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")
