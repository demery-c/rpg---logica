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


#   florestais    #
def florestais():  # def acionada ao ser um boi tata ou mapinguari #
    print(f"\n\n{seu_nome} você é um(a) {racas[sua_raça]}, uma criatura mística nativa das florestas amazonicas.")
    print("OS invasores estão desmatando o seu lar. \nA floresta e todos os habitantes dela estão implorando por ajuda.... \nSem você não tera como eles se protegerem.")
    print("\nVOCÊ DEFENDERA SEU LAR?? .......")
    while True:    ## decisão de jogar ou não (S/N) ##
        escolha = input("S/N: ").upper()
        if escolha == "S":
            fdefesa()
            break
        elif escolha == "N":
            print("\n\nA floresta CHORA ....... GRITOS E MORTE ASSOLAM O LOCAL ....... voCe MorRe jUnTo com a AMAZONia")
            break
        else:
            print("\nEscolha uma opção válida (S/N): ")

def fdefesa():
    print("Você chega para o combate contra os invasores. \n Eles estão armados dos pés a cabeça \nAgora a cobra vai fumar")
    print("\nComo você ira defender sua casa?")
    while True:  
        try:
            escolha = int(input("Agarrar(1), Diálogo(2): "))
            if escolha == 1:
                print("Você segura os invasores com tanta força que eles EXPLODEM!!")
                fataque_agarre()
                break
            elif escolha == 2:
                print("Você conversa com eles e explica que desmatar não é a solução \n eles aprendem e vão embora sem causar destruição")
                fdialogo()
                break
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")

def fdialogo():
    print("\n Após a sua diplomacia os moradores percebem a sua sabedoria, e escolhem te eleger como o ancião da vila ")
    while True:  
        try:
            escolha = int(input("\n Você aceita (1) ou não(2)"))
            if escolha == 1:
                print("Os moradores se alegram com a sua escolha \n todos então começam a iniciar os preparativos para o ritual de passagem")
                break
            elif escolha == 2:
                print("Os moradores se decepicionam com a sua escolha \n Todo então começam a se juntar em volta de você")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")

# ataque #
def fataque_agarre():
    print("\nApós você agarrar os invasores, todos na floresta ficam em choque com a sua agressividade \n Os moradores se juntam e te expulsam da vila ")
    print("\nComo você ira reagir?")
    while True:
        try:
            escolha = int(input("Ira sair(1), Vai matar a vila(2):  "))
            if escolha == 1:
                print("Você cede a pressão dos moradores e vai embora, com o rabo entre as pernas")
                fatque_exilio()
                break
            elif escolha == 2:
                print("Sua ira se instaura em você, o odio na sua veia pulsa...")
                fatque_odio()
                break
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")

def fatque_odio():
    print("\n Com seu odio você aniquila alguns aldeões, mas a vila inteira se junta contra você \n Eles são muitos, seu corpo não suporta")
    print("\n VOCÊ ESTÁ MORTO!")       
    print("\n FINAL RUIM")   
            
def fatque_exilio():
    print("\n Você sai apressadamente da vila, percebendo o que você fez... ")
    while True:
        try:
            escolha = int(input("Seu coração sente odio(1), ou compaixão(2) ?"))
            if escolha == 1:
                print("\n O odio toma conta do seu coração, você quer ter sua vingança! \n Você retorna a vila, armado até os dentes, pronto para exterminar aqueles que te expulsaram")
                print(f"\n {seu_nome} se prontifica e em um ataque surpresa elima todos os seus ex-companheiros \n A vila agora esta em seu comando!")
                print("\n FINAL GENOCIDA")
                break
            elif escolha == 2:
                print("A Compaixão toma conta do seu coração, Você quer se redimir \n Logo você começa a praticar boas ações, e sua reputação aumenta!")
                print(f"Você retorna a vila, os cidadãos percebem a sua mudança {seu_nome} e te acolhem")
                print("\n FINAL REDIMIDO")
                break
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")


#   aquaticos    #
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
    print("\n[1] Os caçadores estão nos matando, alguem faça alguma coisa\n[2] Reuni vocês para coordenarmos as lutas contra os caçadores \n[3] Eu os convoco para lutarmos contra os caçadores. QUEM VEM COMIGO!!!")
    while True:      ## sistema de escolhas de raça ##
        try:
            escolha = int(input("Qual sera sua abordagem???"))
            if escolha == 1 :
                comando_aquatico = 1
                print("Uma guerra ocorre entre os caçadores e vocês \nVocê ve um ser mistico tomando a frente da guerra \nVocê pode dar apoio a ele na luta contra o lider dos caçadores")
            if escolha == 2:               
                comando_aquatico = 2
                print("A guerra se inicia, vocês lutam com diversos caçadores \nDepois de muito tempo o lider dos caçadores vai lutar diretamente com vocês")
            elif escolha == 3:
                comando_aquatico = 3
                print("\n Você organiza a luta contra os caçadores \2Comandando as tropas, você chega diante do lider dos caçadores")
            else:
                print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")



#    jogo rodando    #
personagem()