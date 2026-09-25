"""
Atividade 9
Contexto: Categoria de CNH: A 'Moto', B 'Carro', C 'Caminhão', D 'Ônibus', senão 'Categoria não existe'.
"""

# Escreva seu código abaixo:

categoria = input("Digite a categoria da CNH: ")
if categoria == "A":
    print("Moto")
elif categoria == "B":
    print("Carro")
elif categoria == "C":
    print("Caminhão")
elif categoria == "D":
    print("Ônibus")
else:
    print("Categoria não existe")