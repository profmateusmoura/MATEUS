"""Exemplo 8: acumulando valores.

Explicação:
A soma cresce a cada repetição.
"""

soma = 0

for numero in range(1, 6):
    soma = soma + numero
    print("Agora soma vale:", soma)

print("Resultado final:", soma)
