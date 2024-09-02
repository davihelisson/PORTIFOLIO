# DESAFIO DE PROJETO - DIO
## CRIANDO UM SISTEMA BANCÁRIO COM PYTHON

### IMPLEMENTAÇÕES REQUERIDAS
* 3 OPERAÇÕES: DEPÓSITO, SAQUE, EXTRATO

##### OPERAÇÃO: DEPÓSITO
- Todos os depósitos devem ser armazenados em uma vaiável e exibidos no extrato

##### OPERAÇÃO: SAQUE
- Permitidos apenas 3 saques diários com limite máximo de R$500,00
- Caso não tenha saldo em conta, informar que não será possível realizar a operação por falta de saldo
- Todos os saques devem ser armazenados em uma variável e exibidos no extrato

##### OPERAÇÃO: EXTRATO
- Listar todos os saques e depósitos.
- No final deve exibir o saldo atual da conta
- Valores devem ser no formato float, com duas casas decimais

### DIFERENÇAS / MELHORIAS
1. O Projeto apresentado pelo Guilherme lista as opções com letras. No meu código preferi colocar números (menor chance de teclar errado sem querer querendo)
2. O projeto do Guilherme cria variáveis para verificações dos requisitos:
   * excedeu_saldo = valor > saldo # para ver se o valor solicitado é maior que o saldo
   * excedeu_limite = valor > limite #para ver se o valor solicitado é maior que o limite diário de 500
   * excedeu_saques = numero_saques >= LIMITE_SAQUES #para ver se a operação não excedeu o limite de 3 saques
>> No meu código, preferi manter separadas dentro da lógica IF/ELIF/ELSE por motivos de PQ SIM.
3. Ao selocionar SAIR eu inclui uma mensagem personalizada.

## Feedback
Se você tiver algum feedback, por favor nos deixe saber através de uma issue aqui no GIT
