"""Exercício 17

Faça um programa que peça 3 notas e mostre a média final.

Dica:
Use um laço para ler as três notas e depois divida pela quantidade.
"""

# escreva seu código aqui
soma = 0
for i in range (3):
    notas = int(input("Digite sua nota: "))
    soma = soma + notas
media = soma / 3
print("Sua media foi de: ", media)
    