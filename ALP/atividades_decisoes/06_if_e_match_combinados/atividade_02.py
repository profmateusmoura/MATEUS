"""
ATIVIDADE 02 — Pedido de lanchonete

Leia o código de um item:
1 -> Hambúrguer: R$ 18
2 -> Pizza: R$ 25
3 -> Suco: R$ 8

Use MATCH / CASE para definir nome e preço.
Depois leia a quantidade e use IF para validar se ela é maior que zero.
Mostre o total do pedido.
"""

# ESCREVA SEU CÓDIGO ABAIXO

print('Menu:1 -> Hambúrguer: R$ 18')
print('2 -> Pizza: R$ 25')
print('3 -> Suco: R$ 8')
operador = int(input('Digite o codigo do produto'))
match operador:
    case 1:
      quantidade =  int(input('informe a quantidade de hamburguer'))
      if quantidade > 0:
          print(f'o preço do pedido é{quantidade*18}')
    case 2:
          quantidade =  int(input('informe a quantidade de pizza'))
          if quantidade > 0:
              print(f'o preço do pedido é{quantidade*25}')
    case 3:
          quantidade =  int(input('informe a quantidade de suco'))
          if quantidade > 0:
              print(f'o preço do pedido é{quantidade*8}')
        
        
    