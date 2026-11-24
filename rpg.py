#    variaveis super globais    #
racas = ["boitatá", "mapinguari", "boto", "iara"]
locais = ["cidade", "floresta", "minas"]
armas_iniciais = ["espada", "arco", "martelo"]
dano_inicial = [""]
inimigos_habitantes = ["ladrão", "dromedario", "morcegos"]

seu_nome = ""
sua_raça = ""

slot_arma = ""
slot_1 = ""
slot_2 = ""
slot_3 = ""




#    defs (oque faz o jogo rodar)    #
def personagem():
    global sua_raça, seu_nome
    print("\n\n        SEJA BEM VINDO AO MUNDO DE ELDRIN \n\n")
    nome = input("Qual é o seu nome? : ")
    while True:
        try:
            escolha_raça = int(input("Selecione qual ser você será (1:Boitatá  2:Mapinguari  3:Boto  4:Iara): ")) - 1
            if escolha_raça == 0 or escolha_raça == 1 or escolha_raça == 2 or escolha_raça == 3:
                sua_raça = escolha_raça
                seu_nome = nome
                break
            else:
                print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")


    if sua_raça <= 2:
        florestais()
    else:
        aquaticos()


def florestais():
    print(f"\n\n{seu_nome} você é um {racas[sua_raça]}, uma criatura mística nativa das florestas amazonicas.")
    print("OS invasores estão desmatando o seu lar. \nA floresta e todos os habitantes dela estão implorando por ajuda.... \nSem você não tera como eles se protegerem.")
    print("\nVOCÊ DEFENDERA SEU LAR?? .......")
    while True:
        escolha = input("S/N: ").upper()
        if escolha == "S":
            break 
        elif escolha == "N":
            print("\n\nA floresta CHORA ....... GRITOS E MORTE ASSOLAM O LOCAL ....... voCe MorRe jUnTo com a AMAZONia")
            break
        else:
            print("\nEscolha uma opção válida (S/N): ")

def aquaticos():
    print(f"\n\n{seu_nome} você é um {racas[sua_raça]}, uma criatura mística nativa dos rios amazonicos.")
    print("")




#    jogo rodando    #
personagem()