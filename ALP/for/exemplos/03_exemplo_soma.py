"""Exemplo 3: repetição simples com números.

Explicação:
O for repete um bloco e a variável recebe cada valor da sequência.
"""

soma = 0

for numero in range(1, 6):
    print("Número atual:", numero)
    soma = soma + numero

print("Soma final:", soma)
