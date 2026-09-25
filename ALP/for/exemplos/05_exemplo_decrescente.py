"""Exemplo 5: contagem regressiva.

Explicação:
O terceiro parâmetro do range() indica o passo.

range(5, 0, -1)
- começa em 5
- termina antes de 0
- o passo é -1, então a sequência diminui
- gera: 5, 4, 3, 2, 1

Ou seja, o terceiro parâmetro -1 faz a contagem regressiva.
"""

for numero in range(5, 0, -1):
    print(numero)

print("Fogo!")
