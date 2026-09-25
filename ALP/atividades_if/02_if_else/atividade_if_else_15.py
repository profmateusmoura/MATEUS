"""
Atividade 15
Contexto: Peça um e-mail. Se contiver o caractere '@', imprima 'E-mail válido', senão, 'E-mail inválido'.
"""

# Escreva seu código abaixo:
modulos_salas = ["Primeiro", 207, "Terceiro", 611, "Quarto", 609]
sala = int(input("Digite a sala: "))
if sala in modulos_salas:
    print(f"Sala: {sala} pertence a um dos módulos da escola")
else:
    print("Sala inválida")

email = input("Digite seu e-mail: ")
if "@" in email:
    print("E-mail válido")
else:
    print("E-mail inválido")