"""
Atividade 13
Contexto: Regiões do Brasil por estado: SP/RJ/MG/ES 'Sudeste', PR/SC/RS 'Sul', senão 'Outra região'.
"""

est = input("Qual o estado?")

if (est == "BA" or est == "AL" or est == "MA" or est =="CE" or est == "PE" or est == "SE" or est == "RN" or est =="PI" or est == "PB"):
    print("Nordeste")


elif (est == "MG" or est == "SP" or est == "RJ" or est =="ES"):
    print("Sudeste")

elif(est == "RS" or est == "PR" or est == "SC"):
    print("Sul")

elif (est == "AC" or est == "AP" or est == "AM" or est == "PA" or est == "RO" or est == "RR" or est == "TO"):
    print("Norte")

else:
    print("Centro oeste")






















# Escreva seu código abaixo:
sudeste = ("SP", "RJ", "MG", "ES")
sul = ("PR", "SC", "RS")
norte = ("AC", "AP", "AM", "PA", "RO", "RR", "TO")
nordeste = ("AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE")

estado = input("Digite o estado: ")
if estado in sudeste:
    print("Sudeste")
elif estado in sul:
    print("Sul")
elif estado in norte:
    print("Norte")
elif estado in nordeste:
    print("Nordeste")
else:
    print("Centro-Oeste")

print(sul)
baixo=list(sul)
print(baixo)
baixo[0]="KK"
print(baixo)
del sul
sul = tuple(baixo)
print(sul)




print("Fim do programa")