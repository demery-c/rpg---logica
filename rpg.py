#    variaveis globais    #
import random as r
racas = ["boitatá", "mapinguari", "boto", "iara"]

seu_nome = ""
sua_raça = ""

<<<<<<< HEAD
pureza = 0
=======
pontos_ritual = 0

camando_aquatico = ""
>>>>>>> a958578ea3f4a1993201d74c1562bb7b7273bf0e

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

#   Dialogo     #

def fdialogo():
    print("\n Após a sua diplomacia os moradores percebem a sua sabedoria, e escolhem te eleger como o ancião da vila ")
    while True:  
        try:
            escolha = int(input("\n Você aceita (1) ou não(2)  "))
            if escolha == 1:
                print("Os moradores se alegram com a sua escolha \n todos então começam a iniciar os preparativos para o ritual de passagem")
                fdialogo_aceita()
                break
            elif escolha == 2:
                print("Os moradores se decepicionam com a sua escolha \n Todo então começam a se juntar em volta de você")
                fdialogo_recusa()
                break
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")

def fdialogo_recusa():
    print("Os moradores começam a te empurrar em direção ao centro da vila \n Eles estão te direcionando para a fogueira, você quer reagir?")
    while True:  
        try:
            escolha = input("\n S/N ").upper()
            if escolha == "S":
                print("Você reage contra os habitantes, mas eles são muitos")
                print("\n VOCÊ ESTÁ MORTO!")       
                print("\n FINAL RUIM")   
                break
            elif escolha == "N":
                print("Os moradores te levam até o calabouço... \n Você então é preso pelo resto da sua vida!")
                print("FINAL CARCERÁRIO")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")

def fdialogo_aceita():
    global pontos_ritual
    print("\n O moradores te indicam o que você tem que pegar \n Cinco itens... ")
    inv = 0
    while inv <= 2:
        try:
            escolha = int(input("\n flor dourada(1) \n calice de prata(2) \n pote de cerâmica(3) \n pião(4) \n cocar(5):  "))
            if escolha == 1 or escolha == 2:
                pontos_ritual = pontos_ritual + 5
            elif escolha == 3 or escolha == 4:
                pontos_ritual = pontos_ritual + 10
            elif escolha == 5:
                pontos_ritual = pontos_ritual + 20            
            inv = inv + 1
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
    if pontos_ritual >= 30:
        print("Os sacrificios ritualisticos foram perfeitamente escolhidos... \n você se torna o ancião da vila com respeito máximo")
        print("\n FINAL BOM")
    elif pontos_ritual <= 30:
        print("Os sacrificio ritualisticos não foram perfeitamente escolhidos... \n você se torna o ancião da vila, mas ninguem te respeita")
        print("\n FINAL MÉDIO")


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
    global pureza
    print("Você lembra da velha tradição \nOs botos cantam as margens do rio, e depois descem \nAssim reunindo-os e ordenando em uma crise")
    print("você pode seguir sozinho, ou convocar o chamado das crises, e reunir a sociedade maritima")
    while True:    ## decisão de jogar ou não (S/N) ##
        escolha = input("Chamar a reunião? S/N: ").upper()
        if escolha == "S":
            reunidos() 
        elif escolha == "N":
            input("Você ignora as tradições e ira enfrentar os caçadores sozinho(a)       (Pressione enter para continuar .....)")
            boss_solo()
        else:
            print("\nEscolha uma opção válida (S/N): ")    


def reunidos():
    global comando_aquatico, sua_raça, pureza
    print("os povos maritimos e as criaturas misticas que ali abitam se encontram no fundo do rio \nVocê pode explicar a situação como")
    print("\n[1] Os caçadores estão nos matando, alguem faça alguma coisa\n[2] Reuni vocês para coordenarmos as lutas contra os caçadores \n[3] Eu os convoco para lutarmos contra os caçadores. QUEM VEM COMIGO!!!")
    while True:      ## sistema de escolhas de raça ##
        try:
            escolha = int(input("Qual sera sua abordagem???"))
            if escolha == 1 :
                print("Uma guerra ocorre entre os caçadores e vocês \nVocê ve um ser mistico tomando a frente da guerra \nVocê o segue para apoia-lo na luta contra o lider dos caçadores")
                pureza = 1
            if escolha == 2:               
                print("A guerra se inicia, vocês lutam com diversos caçadores \nDepois de muito tempo o lider dos caçadores vai lutar diretamente com vocês")
                pureza = 2
            elif escolha == 3:
                print("\n Você organiza a luta contra os caçadores \2Comandando as tropas, você chega diante do lider dos caçadores")
                pureza = 3
            else:
                print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
        break
    input("pressione enter para continuar.......")
    boss_solo()

def boss_solo():
    vida = 100
    boss = 100
    atordoado = 0
    ações_boss = ["atirou em você", "te chutou", "te deu um soco"]
    danos = ["40", "20", "30"]
    while boss > 0:
        print("\n\n\n\n\n\n") 
        print(f"Você esta com {vida} de vida")
        print(f"O lider dos caçadores esta com {boss*10} de vida")
        print(f"")
        print("\nSuas ações são")
        try:
            print("[1] encantar (atordoa o inimigo por 2 turnos) \n[2] Soca-lo (30 de dano) \n[3] Jato d'agua (45 de dano, mas so pode ser usado em oponentes atordoados)")
            escolha = int(input("\nOque fara?? : "))
            if escolha == 1:
                atordoado = atordoado + 2
            elif escolha == 2:
                atordoado = atordoado - 1
            elif escolha == 3:
                print("Você da 40")
                input ("pressione enter para continuar........")
                atordoado = atordoado - 1
            else:
                print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")
        except ValueError:
            print("\nEscolha alguma opção dentre as existentes (escreva apenas o numero da opção)")

        if atordoado < 0:
            atordoado = 0
        ação = r.randint(1,3)
        print(f"O lider dos caçadores {ações_boss[ação]}, te tirando {danos[ação]} de dano ")
        input("pressione enter para continuar.......")

<<<<<<< HEAD
def finais():
    global pureza, seu_nome
    if pureza == 0:
        print(f"Você foi um bravo guerreiro(a), e tudo isso sem ninguem saber que {seu_nome} salvou eles")
        print(f"Parabens, você livrou os rios dos caçadores, sem precisar ganhar os creditos")
    elif pureza == 1:
        print(f"Aquele ser que tomou a frente foi proclamado o senhor dos rios amazonicos\nVocê ouve historias de como ele salvou todos eles")
        print(f"Parabens, os rios estão salvos graças ao rei dos rios amazonicos")
    elif pureza == 2:
        print(f"Você e todos os guerreiros dos rios libertaram os proprios rios \nLendas foram feitas de como os rios se defenderam dos caçadores")
        print(f"Parabens os lagos foram salvos")
    elif pureza == 3:
        print(f"Você liderou a guerra contra os caçadores \nCom muita luta vocês salvaram os rios")
        print(f"Os nativos dos rios criaram lendas sobre {seu_nome}, e sua valentia contra os caçadores") 

 

=======
>>>>>>> ab5a41a45862224a246191382ac3a30a8f173cae
#    jogo rodando    #
personagem()