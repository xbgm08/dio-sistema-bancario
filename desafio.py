MENSAGEM_SALDO_INSUFICIENTE = "Operação falhou! Você não tem saldo suficiente."
MENSAGEM_LIMITE_EXCEDIDO = "Operação falhou! O valor do saque excede o limite."
MENSAGEM_SAQUES_EXCEDIDOS = "Operação falhou! Número máximo de saques excedido."
MENSAGEM_VALOR_INVALIDO = "Operação falhou! O valor informado é inválido."
MENSAGEM_USUARIO_CADASTRADO = "Usuário já cadastrado."
MENSAGEM_USUARIO_NAO_ENCONTRADO = "Usuário não encontrado."

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(MENSAGEM_VALOR_INVALIDO)
    return saldo, extrato

def sacar(*, valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
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
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(MENSAGEM_VALOR_INVALIDO)
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
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
        return 
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [ usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_ususario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(MENSAGEM_USUARIO_CADASTRADO)
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logadouro, nro - bairro - cidade/sigla Estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print(f"\nUsuário {nome} cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print(MENSAGEM_USUARIO_NAO_ENCONTRADO)
        return

    print(f"\nConta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}, Titular: {usuario['nome']}")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    print("\n================ CONTAS ================")
    for conta in contas:
        print(f"Agência: {conta['agencia']} - Conta: {conta['numero_conta']} - Titular: {conta['usuario']['nome']}")
    print("========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    MENU = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Cadastrar usuário
        [c] Criar conta
        [l] Listar contas
        [q] Sair

    => """    

    while True:
        opcao = input(MENU)

        if opcao == "d":
            valor = obter_valor("Informe o valor do depósito: ")
            if valor is not None:
                saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "s":
            valor = obter_valor("Informe o valor do saque: ")
            if valor is not None:
                saldo, extrato, numero_saques = sacar(
                    valor=valor, 
                    saldo=saldo, 
                    extrato=extrato, 
                    numero_saques=numero_saques, 
                    limite=limite, 
                    LIMITE_SAQUES=LIMITE_SAQUES
                )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            criar_ususario(usuarios)
        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta) 
        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por usar nosso sistema bancário. Até a próxima!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()