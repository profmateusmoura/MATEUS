def limpar_tela():
    print("\033[H\033[J", end="", flush=True)

saldo = 14.00
while True:    
    limpar_tela()
    print(" =====================================")
    print("# Bem-vindo ao Banco XYZ              #")
    print("# Escolha a operação desejada:        #")
    print(f"#     Saldo atual   {saldo}              #")
    print("# 2 - Sacar                           #")
    print("# 3 - Depositar                       #")
    print("# 9 - Sair                            #")
    print(" =====================================")
    operacao = int(input("Digite o número da operação desejada: "))
    match operacao:
        case 1:
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        case 2:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > saldo:
                print("Não há saldo suficiente!")
            else:
                saldo = saldo - valor_saque
                print("Retire o dinheiro")
                print(f"Seu saldo atual é: R$ {saldo:.2f}")

        case 3:
            deposito = float(input("Informe o valor a ser depositado: "))
            saldo = saldo + deposito
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        case 9:
            break
        case _:
            print("Inválido")

    input("Pressione Enter para continuar...")
 