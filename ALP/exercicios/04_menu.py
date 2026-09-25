"""Exercício 4

Crie um menu simples com 3 opções.
"""

print("Menu:")
print("1 - Ver saldo")
print("2 - Sacar")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Seu saldo é R$ 100,00")
elif opcao == "2":
    print("Você sacou R$ 50,00")
elif opcao == "3":
    print("Saindo...")
else:
    print("Opção inválida")
