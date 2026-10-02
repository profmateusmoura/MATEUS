"""Exemplo 7: tabuada.

Explicação:
A variável numero recebe todos os valores de 1 a 10.
Em cada volta, a operação 5 * numero é calculada.
"""

for numero in range(1, 11):
    for n in range(10,1,-1):
        print(numero, "x", n, "=", numero * n )
        print(numero, "/", n, "=", numero / n )
