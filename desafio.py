MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

MENSAGEM_SALDO_INSUFICIENTE = "Operação falhou! Você não tem saldo suficiente."
MENSAGEM_LIMITE_EXCEDIDO = "Operação falhou! O valor do saque excede o limite."
MENSAGEM_SAQUES_EXCEDIDOS = "Operação falhou! Número máximo de saques excedido."
MENSAGEM_VALOR_INVALIDO = "Operação falhou! O valor informado é inválido."

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print(MENSAGEM_VALOR_INVALIDO)
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print(MENSAGEM_SALDO_INSUFICIENTE)
    elif excedeu_limite:
        print(MENSAGEM_LIMITE_EXCEDIDO)
    elif excedeu_saques:
        print(MENSAGEM_SAQUES_EXCEDIDOS)
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print(MENSAGEM_VALOR_INVALIDO)
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def obter_valor(mensagem):
    valor = input(mensagem)
    if valor.replace('.', '', 1).isdigit():
        return float(valor)
    else:
        print(MENSAGEM_VALOR_INVALIDO)
        return None

while True:
    opcao = input(MENU)

    if opcao == "d":
        valor = obter_valor("Informe o valor do depósito: ")
        if valor is not None:
            saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = obter_valor("Informe o valor do saque: ")
        if valor is not None:
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")