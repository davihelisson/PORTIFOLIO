import datetime
import textwrap

#Utilizando o mesmo sistema criado anteriormente, fazer as seguintes implementações:
#1 - Estabelecer um novo limite de transações diárias (seja saque, depósito, transferência)
#2- Se exceder esse limite, deve informar que esse limite foi excedido, e só poderá fazer novas tranasações no dia seguinte
#3 - Por isso deverá comparar as datas. Além disso deverá mostrar data e hora no extrato de todas as transações.
#4 - Separar as funções anteriores em funções
#5 - Criar duas novas funções: "Cadastrar Cliente" e "Cadastrar Conta Bancária"



def menu():
    menu ='''\n
    =============== MENU ===============

    SELECIONE UMA DAS OPÇÕES ABAIXO:

    [1] - Cadastrar Novo Cliente
    [2] - Cadastrar Nova Conta Bancária
    [3] - Consultar Extrato
    [4] - Sacar
    [5] - Depositar
    [6] - Listar Contas

    [0] - SAIR
    ====================================
    '''
    return input(textwrap.dedent(menu))


#Implementações Avançadas - Eu assisti essas aulas? Ainda não...
# Decorador de LOG - decorador que registra a data e hora de cada transação, além do tipo de transação
# Gerador de Relatórios - iterando sobre as transações retornar as que foram realizadas. Também incluir um filtro com base no tipo de operação
# Iterador personalizado - quando selecionar a opção de listar contas, deve mostrar todas as contas cadastradas, com nome, CPF, conta, Agência, e Saldo

def log_transacao(func):
    def envelope(*args, **keyargs):
        resultado = func(*args, **keyargs)
        print(f"{datetime.now}: {func.__name__.upper()}")
        return resultado
    return envelope



def depositar(saldo, deposito, extrato, /):#Essa barra serve para indicar que essa função é POSITIONAL ONLY (tudo antes dela só é acessado pela posição)
    #Nessa parte é para colocar aqueles IF's e ELSE's que estavam no outro código
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f}\n"
        print(f"Depositando...\nSaldo atual: R${saldo:.2f} \nDepósito Realizado com Sucesso!")
    else:
        print("Valor inválido. Saques devem ser maiores que R$0.00")
    return saldo, extrato


def sacar(*, saldo, saque, extrato, valor_limite_saque, quant_limite_saques, numero_saques):
    #Esse asterísco no começo é para forçar que essa função seja KEYWORD ONLY (nomeados)
    if numero_saques <= quant_limite_saques:
        if saldo > saque and saque <= 500 and saque < valor_limite_saque:
            saldo -= saque
            numero_saques += 1
            extrato += f"Depósito: R${saque:.2f}\n"
            print(f"\nSaque realizado com Sucesso!\nSaldo atual: R${saldo}")
        elif saque <= 0:
            print("Valor inválido. Digite valores acima de R$ 0.00")
        else:
            print("OPERAÇÃO NÃO FOI REALIZADA.\nValor acima do limite diário ou Saldo insulficiente!")
    else:
        print("Limite de saques diários atingido. Tente novamente outro dia.")

    return saldo, extrato



def extrato(saldo, /, *, extrato): #Saldo é posicional, Extrato é nomeado
    print('''========== EXTRATO ==========''')
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print('''========== ======= ==========''')


def cadastrar_cliente(usuarios):
    #Essa aqui é a primeira implementação - CRIAR UMA LISTA DE CLIENTES
    cpf = input("Informe seu CPF (Somente Números): ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\nJÁ EXISTE UM USUÁRIO COM ESSE CPF.")
        return

    nome = input("Insira o NOME COMPLETO do cliente: ")
    data_nasc = input("Insira a Data de Nascimento: ")
    endereco = input("Insira o endereço completo (Rua, nº, bairro, cidade/UF): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("====== USUÁRIO CADASTRADO COM SUCESSO!=====")

def filtro_usuario(cpf, usuarios):#Essa função é para comprimir uma lista de usuários e fazer um filtro
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    #Nessa lista aqui de cima, se o CPF digitado for igual a algum CPF digitado anteriror mente, retorno para o "USUÀRIO" onde tem a msg de erro.
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n CCONTA CRIADA COM SUCESSO!")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario": usuario}

    print("\nUsuário não foi encontrado. Retorne ao menu e insira o Usuário no Sistema.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        Conta: \t{conta['numero_conta']}
        Titular: \t{conta['usuario'],['nome']}"""
        print("="*100)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    valor_limite_saque = 1000
    extrato = ""
    numero_saques = 0
    quant_limite_saques = 5

    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        # OPERAÇÃO: CADASTRAR NOVO CLIENTE
        if opcao == 6:
             listar_contas(contas)

        # OPERAÇÃO: DEPÓSITO
        elif opcao == 5:
            deposito = float(input("Digite o valor a ser depositado: R$"))
            # O código anterior colocava todos os IF's e Elses aqui. Agora vem as funções
            saldo, extrato = depositar(saldo, deposito, extrato)

        #OPERAÇÃO: SAQUE
        elif opcao == 4:
            saque = float(input("Digite o valor a ser sacado: R$"))
            saldo, extrato = sacar(
            saldo=saldo,
            saque=saque,
            extrato=extrato,
            valor_limite_saque=valor_limite_saque,
            quant_limite_saques=quant_limite_saques,
            )

        # OPERAÇÃO: EXTRATO
        elif opcao == 3:
           extrato(saldo, extrato=extrato)



        # OPERAÇÃO: CADASTRAR NOVA CONTA BANCÁRIOA
        elif opcao == 2:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        # OPERAÇÃO: CADASTRAR NOVO CLIENTE
        elif opcao == 1:
               cadastrar_cliente(usuarios)


        # OPERAÇÃO: SAIR DO SISTEMA
        elif opcao == 0:
            print('''
            Obrigado por utilzar nossos serviços!
            Volte sempre.''')
            break

        else:
            print("Opção inválida! Por favor, selecione novamente a opção desejada:")


main()