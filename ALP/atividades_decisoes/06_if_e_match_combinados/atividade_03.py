"""
ATIVIDADE 03 — Calculadora segura

Leia dois números e uma operação (+, -, *, /).
Use MATCH / CASE para escolher a operação.
Quando a operação for divisão, use IF para impedir divisão por zero.
"""

# ESCREVA SEU CÓDIGO ABAIXO



numero_1 = float(input("Digite o primeiro número"))
numero_2 = float(input("Digite o segundo número"))
operacao = (input("Escolha a operação entre + - * e / "))

match operacao:
    case '+':
        resultado = numero_1 + numero_2
        print(f"O resultado é: {resultado}")
    case '-':
            resultado = numero_1 + numero_2
            print(f"O resultado é: {resultado}")
    case '*':
            resultado = numero_1 + numero_2
            print(f"O resultado é: {resultado}")
    case '/':
            if(numero_2 == 0):
                print(f"Erro na divisão")
            else:
                resultado = numero_1 + numero_2
                print(f"O resultado é: {resultado}")
    case _:
        print("Erro na operação")