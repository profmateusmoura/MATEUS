"""
Atividade 1
Contexto: Classifique a idade: <=12 'Criança', 13 a 17 'Adolescente', 18 a 59 'Adulto', >=60 'Idoso'.
"""

# Escreva seu código abaixo:

idade = int(input("Digite a idade: "))
if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")