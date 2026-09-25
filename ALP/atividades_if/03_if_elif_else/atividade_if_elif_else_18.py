"""
Atividade 18
Contexto: Estado físico da água pela temperatura: < 0 'Sólido', 0 a 99 'Líquido', >= 100 'Gasoso'.
"""

# Escreva seu código abaixo:

temperatura = float(input("Qual a temp em °C? "))

if temperatura >= 100:
    print("Evaporou!")
elif temperatura < 0:
    print("Congelou!")
else:
    print("Líquido")