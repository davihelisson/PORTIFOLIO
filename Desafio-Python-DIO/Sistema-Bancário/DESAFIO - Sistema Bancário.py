#DESAFIO DE CÓDIGO
#IMPLEMENTAR 3 OPERAÇÕES: DEPÓSITO, SAQUE, EXTRATO

menu = ('''
    =============== MENU ===============

    SELECIONE UMA DAS OPÇÕES ABAIXO:

    [1] - Consultar Extrato
    [2] - Sacar
    [3] - Depositar

    [0] - SAIR
    ====================================
    '''
)

saldo = 0
valor_limite_saque = 500
extrato = ""
numero_saques = 0
num_limite_saques = 3

while True:
    opcao = int(input(menu))

#OPERAÇÃO: DEPÓSITO
#Todos os depósitos devem ser armazenados em uma vaiável e exibidos no extrato
    if opcao == 3:
        deposito = float(input("Digite o valor a ser depositado: R$"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"Depositando...\nSaldo atual: R${saldo:.2f}")
        else:
            print("Valor inválido. Saques devem ser maiores que R$0.00")

#OPERAÇÃO: SAQUE
# Permitidos apenas 3 saques diários com limite máximo de R$500,00
# Caso não tenha saldo em conta, informar que não será possível realizar a operação por falta de saldo
# Todos os saques devem ser armazenados em uma variável e exibidos no extrato
    elif opcao == 2:
        if numero_saques <= num_limite_saques:
            saque = float(input("Digite o valor a ser sacado: R$"))
            if saldo > saque and saque <= 500 and saque < valor_limite_saque:
                saldo -= saque
                numero_saques += 1
                extrato += f"Depósito: R${saque:.2f}\n"
                print(f"Saque realizado com Sucesso!\nSaldo atual: R${saldo}")
            elif saque <= 0:
                print("Valor inválido. Digite valores acima de R$ 0.00")
            else:
                print("OPERAÇÃO NÃO FOI REALIZADA.\nValor acima do limite diário ou Saldo insulficiente!")
        else:
            print("Limite de saques diários atingido. Tente novamente outro dia.")


#OPERAÇÃO: EXTRATO
#Listar todos os saques e depósitos.
# No final deve exibir o saldo atual da conta
# Valores devem ser no formato float, com duas casas decimais
    elif opcao == 1:
        print('''========== EXTRATO ==========''')
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print('''========== ======= ==========''')

    elif opcao == 0:
        print('''
        Obrigado por utilzar nossos serviços!
        Volte sempre.''')
        break

    else:
        print("Opção inválida! Por favor, selecione novamente a opção desejada:")