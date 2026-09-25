"""
ATIVIDADE 03 — Mini sistema de pedidos

Leia uma categoria:
1 - Bebida
2 - Lanche
3 - Sobremesa

Depois leia um código dentro da categoria:

Bebida:
1 -> Água R$ 4
2 -> Suco R$ 8

Lanche:
1 -> Sanduíche R$ 15
2 -> Pizza R$ 22

Sobremesa:
1 -> Sorvete R$ 10
2 -> Bolo R$ 12

Leia quantidade, valide e calcule o total.
Você pode usar MATCH / CASE aninhado ou combinar MATCH e IF.
"""

print("1 - Bebida")
print("2 - Lanche")
print("3 - Sobremesa")
cat = int (input("Escolha a categoria: "))

match(cat):
    case 1:
        print("1 -> Água R$ 4")
        print("2 -> Suco R$ 8")
        cod = int(input("Digite o código: "))
        qtd = int(input("Digite a quantidade: "))
        if(qtd>0):            
            match(cod):
                case 1:
                    preco = 4.00
                case 2:
                    preco = 8.00
            total=qtd*preco
            print(f"O total é {total:.2f}")   
        else:
            print("Quantidade inválida!")          
    case 2:
        print("1 -> Sanduíche R$ 15")
        print("2 -> Pizza R$ 22")
        cod = int(input("Digite o código: "))
        qtd = int(input("Digite a quantidade: "))
        if(qtd>0):            
            match(cod):
                case 1:
                    preco = 15.00
                case 2:
                    preco = 22.00
            total=qtd*preco
            print(f"O total é {total:.2f}")   
        else:
            print("Quantidade inválida!")  
    case 3:
        print("1 -> Sorvete R$ 10")
        print("2 -> Bolo R$ 12")
        cod = int(input("Digite o código: "))
        qtd = int(input("Digite a quantidade: "))
        if(qtd>0):            
            match(cod):
                case 1:
                    preco = 10.00
                case 2:
                    preco = 12.00
            total=qtd*preco
            print(f"O total é {total:.2f}")   
        else:
            print("Quantidade inválida!")  



#match/ cases para menus e if's para validações