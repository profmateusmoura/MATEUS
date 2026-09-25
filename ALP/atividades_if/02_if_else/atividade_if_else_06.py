"""
Atividade 6
Contexto: Pergunte a hora atual (0 a 23). Se for entre 8 e 18, imprima 'Loja aberta', senão, 'Loja fechada'.
"""
hora = int(input("Que hora é essa aí?"))
#if (hora >= 8 and hora <= 18):
    #print("Tá aberto!")
#else:
    #print("Volte outro dia!")
if (hora < 8 or hora > 18):
    print("Volte outro dia!")
else:
    print("Tá aberto!")

#if not(hora < 8 or hora > 18):
    #print("Tá aberto!")
#else:
    #print("Volte outro dia!")