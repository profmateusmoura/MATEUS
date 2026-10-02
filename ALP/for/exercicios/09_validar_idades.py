"""Exercício 9

Dada uma lista de idades, mostre apenas as maiores de 18.

Dica:
Use if dentro do laço para filtrar as idades.
"""

# escreva seu código aqui
idades = [12,43,54, 18,32,21,16]
for idade in idades:
    if idade > 18:
        print(idade)