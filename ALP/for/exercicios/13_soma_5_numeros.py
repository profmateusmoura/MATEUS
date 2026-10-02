"""Exercício 13

Peça 5 números e mostre a soma deles.

Dica:
Use um laço para repetir 5 vezes e acumular a soma.
"""

# escreva seu código aqui
soma = 0
for i in range (5):
    numero = int(input("Digite um numero: "))
    soma = soma + numero
print("A soma é:", soma)
