#    variaveis globais    #

racas = ["boitatá", "mapinguari", "boto", "iara"]

seu_nome = ""
sua_raça = ""

camando_aquatico = ""

#    defs (oque faz o jogo rodar)    #
def personagem():
    global sua_raça, seu_nome
    print("\n\n        SEJA BEM VINDO AO MUNDO DE ELDRIN \n\n")
    nome = input("Qual é o seu nome? : ")
    while True:      ## sistema de escolhas de raça ##
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

    ## caminhos possiveis (de acordo com a raça escolhida) ##
    if sua_raça == 0 or sua_raça == 1:
        florestais()
    else:
        aquaticos()

def florestais():  # def acionada ao ser um boi tata ou mapinguari #
    print(f"\n\n{seu_nome} você é um(a) {racas[sua_raça]}, uma criatura mística nativa das florestas amazonicas.")
    print("OS invasores estão desmatando o seu lar. \nA floresta e todos os habitantes dela estão implorando por ajuda.... \nSem você não tera como eles se protegerem.")
    print("\nVOCÊ DEFENDERA SEU LAR?? .......")
    while True:    ## decisão de jogar ou não (S/N) ##
        escolha = input("S/N: ").upper()
        if escolha == "S":
            break 
        elif escolha == "N":
            print("\n\nA floresta CHORA ....... GRITOS E MORTE ASSOLAM O LOCAL ....... voCe MorRe jUnTo com a AMAZONia")
            break
        else:
            print("\nEscolha uma opção válida (S/N): ")

def aquaticos():  # def acionada ao ser um boto ou iara #
    print(f"\n\n{seu_nome} você é um(a) {racas[sua_raça]}, uma criatura mística nativa dos rios amazonicos.")
    print("Você ouve relatos de que os caçadores estão atras dos animais marinhos \nSupostamente vocês estão iludindo cidadões e matando-os afogados \nVocê precisa ajudar os animais do grande rio amazonico") 
    print("\nVOCÊ ENFRENTARA OS CAÇADORES?? .......")
    while True:    ## decisão de jogar ou não (S/N) ##
        escolha = input("S/N: ").upper()
        if escolha == "S":
            a_reunião() 
        elif escolha == "N":
            print("\n\nUm tempo se passa ....... CORPOS APARECEM AS MARGEMS DO RIO ....... sEM VocÊ todAs AS criAturAs morReRam")
            break
        else:
            print("\nEscolha uma opção válida (S/N): ")

def a_reunião():
    print("Você lembra da velha tradição \nOs botos cantam as margens do rio, e depois descem \nAssim reunindo-os e ordenando em uma crise")
    print("você pode seguir sozinho, ou convocar o chamado das crises, e reunir a sociedade maritima")
    while True:    ## decisão de jogar ou não (S/N) ##
        escolha = input("S/N: ").upper()
        if escolha == "S":
            reunidos() 
        elif escolha == "N":
            input("Você ignora as tradições e ira enfrentar os caçadores sozinho(a)       (Pressione enter para continuar .....)")
            break
        else:
            print("\nEscolha uma opção válida (S/N): ")    

def reunidos():
    global comando_aquatico, sua_raça
    print("os povos maritimos e as criaturas misticas que ali abitam se encontram no fundo do rio \nVocê pode explicar a situação como")
    print("[1] Os caçadores estão nos matando, alguem faça alguma coisa\n[2] Reuni vocês para coordenarmos as lutas contra os caçadores \n[3] Eu e mais 2 pessoas lutaremos contra os invasores... Quem se voluntaria")
    while True:      ## sistema de escolhas de raça ##
        try:
            escolha = int(input("Qual sera sua abordagem???"))
            if escolha == 1 :
                comando_aquatico = 1
            if escolha == 2:               
                comando_aquatico = 2
            elif escolha == 3:
                comando_aquatico = 3
                print("Você organiza a luta contra os caçadores \2Com uma ")
            else:
                print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")



#    jogo rodando    #
personagem()