from abc import ABC, abstractproperty, abstractclassmethod
from _datetime import datetime
import textwrap


# Atualizar a implementação do sistema anterior, para armazenar os dados dos clientes em objetos ao invés de dicionários.

# Passo 01 - Criar uma classe Cliente (Classe-Pai)
class Cliente: #Classe-pai
    def __init__(self, endereco): # Construtor
        self.endereco = endereco
        self.contas = [] # O cliente começa a operação sem uma conta.

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta) # A conta digitada será adicionada na lista acima.


class PessoaFisica(Cliente): #Classe-filha para pedar as informações do usuário e consensá-las em 'endereço'
    def __init__(self, nome, dtnasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.dtnasc = dtnasc
        self.cpf = cpf

# Passo 02 - Criar uma classe para Conta
class Conta:
    def __init__(self, numero, cliente): #Classe construtora padrão: todos as variáveis são 'privados'
        self._saldo = 0
        self._numero = numero #Esse numero corresponde ao numero da conta
        self._agencia = '0001' # todas as contas vão ter a agência como '0001'
        self._cliente = cliente
        self._historico = Historico() # Veja a classe Histórico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente) #retorna as instãncias da classe Conta - veja os argumentos dentro do construtor.

# Os próximos métodos são para mapear as propriedades da 'Conta' definidos no construtor
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia (self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

# Agora os próximos métodos vão ser para definir as operações bancárias SAQUE, DEPÓSITO, SALDO E CRIAR NOVA CONTA
# São argumentos públicos (não iniciam com um underline)
    def sacar(self, valor):
        saldo = self.saldo #referência para a propriedade 'saldo'
        excedeu_saldo = valor > saldo #verificação para ver se o valor solicitado é maior que o saldo

        if excedeu_saldo: #Se o valor for maior que o saldo:
            print("\nOPERAÇÃO NÃO FOI REALIZADA.\nSaldo insulficiente!")

        elif valor < 0: #Se o valor for negativo:
            print("Valor inválido. Digite valores acima de R$ 0.00")

        else: # Se passou pelos filtros anteriore, então o valor solicitado é positivo e não é mairo que o saldo.
            self._saldo -= valor
            print(f"\nSaque realizado com Sucesso!\nSaldo atual: R${self.saldo:.2f}")
            return True #Só pra identificar que a operação deu certo

        return False #Para indicar que a operação não deu certo.

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depositando...\nSaldo atual: R${self.saldo :.2f} \n====Depósito Realizado com Sucesso!====")
        else:
            print("Valor inválido. Saques devem ser maiores que R$0.00")
            return False

        return True



# O próximo bloco é para a classe de "Conta Corrente" que é uma classe-filha de 'Conta'
# A diferênça é que aqui podemos inserir um limite de saques e um valor limite para sacar

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=600, limite_saques=4): #Construtor
        super().__init__(numero, cliente)
        self.limite = limite #atributo padrão de limite de valor: $600
        self.limite_saques = limite_saques #limite de saques por dia: 4

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao["tipo"] == Saque.__name__])
        '''
        Explicando melhor o código acima, eu estou iterando uma lista de transações armazenadas no 'histórico'
        e verificando se o "tipo" é igual a "Saque", e contando quantas vezes isso ocorre (por isso estou usando o len().
        O resultado dessa verificação é armazenado na variável "numero_saque".
        '''

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\nValor acima do limite diário!")
        elif excedeu_saques:
            print("\nNúmero máximo de saques diários excedido")
        else: #Se não exceder o valor limite e nem o limite diário de saques
            return super().sacar(valor) #Chamar o 'sacar' do método pai definido na conta. Eis então o conceito de herança

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta Corrente:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Finalmente vamos colocar o HISTÓRICO de operações.
# Essa classe anteriormente estava entrando como uma lista no extrato. Agora ela será armezenada em uma classe própria.
# Como o usuário não pode ter acesso de alterar os dados do histórico, os atributos terão que ser privados
class Historico:
    def __init__(self):
        self._transacoes = [] #todas as transações serão armazenadas em uma lista

    @property
    def transacoes(self):
        return self._transacoes #propriedade para pegar as transações

    def adicionar_transacoes(self, transacao): #vai receber uma transação
        self._transacoes.append(               #vai armazenar ela na lista de transações como conjunto chave:valor
            {
                "tipo": transacao.__class__.__name__,                   #nome da transação (saque, depósito)
                "valor": transacao.valor,                                #valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),  #data e hora da transação
            }
        )

# Agora iremos adicionar uma interface de TRANSAÇÃO (classe abstrata do módulo ABC)
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

# Finalmente, vamos mapear o saque e o depósito em classes-filhas da classe 'Transacao'
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao: #Se a operação sacar der certo, vai ser armazenado no histórico
            conta._historico.adicionar_transacoes(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta._historico.adicionar_transacoes(self)


'''
Agora vamos implementar a parte do menu para funcionar junto com as classes.
Muita coisa será copiada do desafio com data&hora
'''
def menu():
    menu ='''\n
    ===================== MENU =====================
    
    DIGITE UM NÚMERO PARA SELECIONAR UMA DAS OPÇÕES ABAIXO:

    [1] - Cadastrar Novo Cliente
    [2] - Cadastrar Nova Conta Bancária
    [3] - Consultar Extrato
    [4] - Sacar
    [5] - Depositar
    [6] - Listar Contas

    [0] - SAIR
    ===============================================================
    '''
    return input(textwrap.dedent(menu))

def cadastrar_cliente(clientes):
    CPF = input("Informe o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(CPF, clientes)

    if cliente:
        print("\nJÁ EXISTE UM USUÁRIO COM ESSE CPF.")
        return

    nome = input("Insira o NOME COMPLETO do cliente: ")
    data_nasc = input("Insira a Data de Nascimento: ")
    endereco = input("Insira o endereço completo (Rua, nº, bairro, cidade/UF): ")

    cliente = PessoaFisica(nome=nome, dtnasc=data_nasc, endereco=endereco, cpf=CPF)
    clientes.append(cliente)

    print("====== USUÁRIO CADASTRADO COM SUCESSO!=====")


def cadastrar_conta(numero_conta, clientes, contas):
    CPF = input("Informe o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(CPF, clientes)

    if not cliente:
        print("Cliente não foi encontrado. \n\nSelecione a opção [1] no menu e cadastre o cliente.")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n CCONTA CRIADA COM SUCESSO!")
    return {"numero_conta": numero_conta, "usuario": cliente}


def extrato(clientes):
    CPF = input("Informe o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(CPF, clientes)

    if not cliente:
        print("Cliente não foi encontrado")
        return

    conta = recuperar_conta_clientes(cliente)
    if not conta:
        return

    print('''========== EXTRATO ==========''')
    transacoes = conta._historico.transacoes #para exibiro o extrato, preciso ter acesso ao histórico de transações

    extrato = ""
    if not transacoes:
       extrato =  "Não foram realizadas operações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo Atual: R$ {conta.saldo:.2f}")
    print('''========== ======= ==========''')

def sacar(clientes):
    CPF = input("Informe o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(CPF, clientes)

    if not cliente:
        print("Cliente não foi encontrado")
        return

    valor = float(input("Informe o valor do SACAR: R$"))
    transacao = Saque(valor)  # registrar a transação e aparecer no histórico

    conta = recuperar_conta_clientes(cliente) # Como temos um cliente, temos acesso à conta
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def depositar(clientes):
    CPF = input("Informe o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(CPF, clientes)

    if not cliente:
        print("Cliente não foi encontrado")
        return

    valor = float(input("Informe o valor do DEPÓSITO: R$"))
    transacao = Deposito(valor) #registrar a transação e aparecer no histórico

    conta = recuperar_conta_clientes(cliente) # Agora estamos verificando se o cliente possui uma conta
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def filtrar_cliente(CPF, clientes):
    # Aqui listamos os clientes que contenham o CPF igual ao CPF inserido no início do código
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == CPF]

    # Havendo um cliente com o CPF solicitado, o programa deve retornar o item que estiver na primeira referência
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_clientes(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.\nSelecione a opção [2] no menu para Criar uma Nova Conta")
        return
    else:
         return cliente.contas[0]

def listar_contas(contas):
     for conta in contas:
         print("="*100)
         print(textwrap.dedent(str(conta)))


# ____________________________________________________________________________________________________________________
# Uma das principais mudanças é no MAIN()
# Os limites de saque, saldo inicial, extrato, numero da agência estão em classes distintas,
# Não estão mais declaradas como default

def main():
    clientes = [] # As únicas coisas que interessam ser armazenadas no Banco são os clientes e suas contas
    contas = []

    while True:
        opcao = menu()

        # OPERAÇÃO: CADASTRAR NOVO CLIENTE
        if opcao == '1':
            cadastrar_cliente(clientes)

        # OPERAÇÃO: CADASTRAR NOVA CONTA BANCÁRIA
        elif opcao == '2':
            numero_conta = len(contas) + 1
            cadastrar_conta(numero_conta, clientes, contas)

        # OPERAÇÃO: EXIBIR EXTRATO
        elif opcao == '3':
            extrato(clientes)

        # OPERAÇÃO: SAQUE
        elif opcao == '4': # Lembra da quantidade de argumentos que tinhamos que declarar?
            sacar(clientes)

        # OPERAÇÃO: DEPÓSITO
        elif opcao == '5':
            depositar(clientes)

        # OPERAÇÃO: LISTAR CONTAS
        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '0':
            break

main()
