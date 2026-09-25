"""Exercício 3

Peça a nota e mostre se o aluno foi aprovado, em recuperação ou reprovado.
"""

nota = float(input("Digite a nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
