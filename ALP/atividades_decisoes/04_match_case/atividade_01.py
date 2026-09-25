"""
ATIVIDADE 01 — Número por extenso

Leia um número inteiro de 1 a 5 e mostre seu nome por extenso.
Exemplo:
Entrada: 3
Saída: três

Use MATCH / CASE.
Inclua um CASE _ para valores inválidos.
"""

# ESCREVA SEU CÓDIGO ABAIXO

numero_inteiro = (input("Digite um numero entre 1 e 5"))
match numero_inteiro:
    case '1':
        print("Um")
    case '2':
            print("Dois")
    case '3':
            print("Treis")
    case '4':
            print("Quatro")
    case '5':
            print("Cinco")
    case _:
        print("Valor Invahlido")