"""Exemplo 1: repetição simples com for sem range.

Explicação:
O comando for percorre uma sequência de itens.
Aqui a sequência é a palavra "Python".

Estrutura:
for letra in "Python":
    print(letra)

Significado:
- for = para cada item
- letra = variável que recebe o valor atual
- in = indica a sequência
- "Python" = sequência de caracteres

A cada volta do laço, a variável letra recebe uma letra diferente:
P, y, t, h, o, n.
"""
import string

list = (string.ascii_uppercase)
#for letra in list :
#    print(letra)
    
for i in range (1, len(list), 2):
    print(list[i])
