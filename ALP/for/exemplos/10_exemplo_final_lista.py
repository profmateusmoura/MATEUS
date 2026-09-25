import os

lista_de_chamada = [
    "ADSON",
    "ANDERSON",
    "ARTHUR",
    "CAMILA",
    "CARLA",
    "CARLOS",
    "DANIEL",
    "DAVI JEFERSON",
    "DAVID JÚNIO",
    "DIEGO",
    "EDUARDO",
    "ELLEN",
    "FLÁVIA",
    "GABRIELA",
    "GEOVANA",
    "GUILHERME",
    "GUSTAVO",
    "JOÃO VÍCTOR GONÇALVES",
    "JOÃO VÍTOR CORREA",
    "JOÃO VITOR DE PAIVA",
    "JOYCE",
    "JOSEPH",
    "KAUÂ",
    "KAYKY",
    "LEONARDO",
    "LUCAS",
    "LUIS",
    "MARIA EDUARDA",
    "MARIA VITÓRIA",
    "MATHEUS",
    "MICHEL",
    "RICARDO",
    "SANZIO",
    "THIAGO",
    "YAN"
]

print("ATENÇÃO: LISTA DE CHAMADA DA TURMA")
print("====================================")
print("Pressione ENTER para iniciar a chamada...")
input()

for indice, nome in enumerate(lista_de_chamada, start=1):
    os.system("cls")
    print("ATENÇÃO: CHAMADA EM ANDAMENTO")
    print("============================")
    print(f"{indice}º nome da lista")
    print()

    if indice == 1:
        print("=> PRIMEIRO NOME: ", nome)
    else:
        print("=> CHAMANDO: ", nome)

    print()
    print("Aguarde... pressione ENTER para continuar")
    input()

print("FIM DA CHAMADA")
