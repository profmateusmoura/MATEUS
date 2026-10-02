"""Exercício 16

Dada uma lista de idades, conte quantas pessoas são maiores de 18 anos.

Dica:
Use uma variável para contar e um if dentro do laço.
"""

# escreva seu código aqui
lista = [10, 12 , 22 , 34, 52, 33]
carlos = 0
for i in lista:
    if i > 18:
        carlos = carlos + 1
print(carlos)