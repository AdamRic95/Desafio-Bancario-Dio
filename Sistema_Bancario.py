def menu(): 
    menu = """
            Bem vindo a Banco Novo:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar as Contas
    [6] Novo Usuário
    [0] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+=valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"=== Depósito de R${valor:.2f} efetuado com sucesso.===\n")
        print(f"=== Novo saldo: R${saldo:.2f} ===")
    else:
        print("### Falha na Operação ###\n")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    saldo_insuficiente = valor > saldo 
    limite_excedido = valor > limite 
    excedeu_limite = numero_saques > LIMITE_SAQUES

    if saldo_insuficiente:
        print("### Falha na operação - Saldo Insuficiente ###")

    elif limite_excedido:
        print("### Falha na operação - Valor de saque excede o limite")

    elif excedeu_limite:
        print("### Falha na operação - Limite de saques excedido ###")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"=== Saque de R${valor:.2f} efetuado com sucesso.===\n")
        print(f"=== Novo saldo: R${saldo:.2f} ===")

    else:
        print("\n ### Falha na operação - Insira valor válido. ###")

    return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}\n")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Já existe usuário com esse CPF ###")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com Sucesso. ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n\t ### Usuário não encontrado - Criação de conta encerrada! ###")

def listar_contas(contas):
    if not contas:
        print("\n\t=== Nenhuma conta foi criada ainda!===\n")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
"""
        print("=" *100)
        print(linha)






def main():
    saldo = 500
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len (contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("### Operação inválida, por favor selecione novamente a operação desejada. ###")

main()