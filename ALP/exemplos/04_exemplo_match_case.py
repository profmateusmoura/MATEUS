"""Exemplo 4: estrutura match/case.

Explicação:
O match case compara uma variável com vários valores possíveis.
É útil quando temos muitas opções.
"""

opcao = "2"

match opcao:
    case "1":
        print("Entrou na opção 1")
    case "2":
        print("Entrou na opção 2")
    case "3":
        print("Entrou na opção 3")
    case _:
        print("Opção inválida")
