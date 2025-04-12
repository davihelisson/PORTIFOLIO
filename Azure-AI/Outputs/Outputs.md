# Outputs

Saídas geradas pelo Copilot, tomando como base os inputs dispostos na pasta Inputs.


### Saídas de Código:
1) Gere um código em Pyton para calcular o n-esimo numero da sequência de Fibonacci usando funções recursivas
```
def fat(n):
    if n ==1 or n == 0:
        return 1
    else:
        return n * fat(n-1)
print (fat(4))
```

2) Gere um código em Python para verificar se um número é par ou Ímpar
```
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(eh_primo(17))  # True
```

3) Crie um código em JavaScrip que inverta uma String
```
function inverterString(str) {
    return str.split('').reverse().join('');
}

console.log(inverterString("OpenAI"));  // "IAnepO"
```

