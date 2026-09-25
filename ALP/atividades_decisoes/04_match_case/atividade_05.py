"""
ATIVIDADE 05 — Operação matemática

Leia dois números e depois um operador:
+  -  *  /

Use MATCH / CASE para escolher a operação e mostrar o resultado.
Na divisão, considere também a possibilidade de o segundo número ser zero.
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

            

            resultado = numero_1 + numero_2
            print(f"O resultado é: {resultado}")
    case _:
        print("Erro na operação")