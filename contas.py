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
