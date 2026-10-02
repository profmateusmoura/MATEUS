"""Exemplo 6: calcular a média de três notas."""

quantidade = 1
soma = 0

while quantidade <= 3:
    nota = float(input("Digite uma nota: "))
    soma = soma + nota
    quantidade = quantidade + 1

media = soma / 3
print("Média:", media)
