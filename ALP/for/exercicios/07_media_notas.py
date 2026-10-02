"""Exercício 7

Calcule a média de 5 notas.

Dica:
Some todas as notas e divida pela quantidade de notas.
"""

# escreva seu código aqui
soma=0
nota=[3.0, 9.0, 4.0, 5.0]
for numero in nota:
    print(numero)
    soma=soma+numero
print("A soma total foi:", soma, "Ja a media foi:", soma/len(nota))