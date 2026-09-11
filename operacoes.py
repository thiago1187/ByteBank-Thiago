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


def pix(conta):
    chave_destino = input("Chave pix de destino: ").strip()
    destino = contas.buscar_por_chave(chave_destino)
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
    print(f"Pix de R$ {valor:.2f} enviado para {destino['nome']}. Saldo: R$ {conta['saldo']:.2f}")
