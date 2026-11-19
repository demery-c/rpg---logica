#    variaveis globais    #
racas = ["humano", "elfo", "anão", "draconico"]
locais = ["cidade", "floresta", "minas"]
armas_iniciais = ["espada", "arco", "martelo"]
dano_inicial = [""]
inimigos_habitantes = ["ladrão", "goblin", "morcegos"]

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
        escolha_raça = int(input("Selecione sua raça (1:Humano  2:Elfo  3:Anão) : ")) - 1
        if escolha_raça == 0 or escolha_raça == 1 or escolha_raça == 2:
            sua_raça = escolha_raça
            seu_nome = nome
            break
        else:
            print("\nNão ouve uma escolha valida, por favor selecione uma escolha valida")






#    jogo rodando    #
personagem()
print("\n Você acorda em um local estranho, com um mapa ao seu lado")
print(".... \n Você olha o mapa e percebe 3 direções distintas")
print("Cada direção tem um simbolo, eles são .... \n Um muro de tijolos \n Uma arvore \n Uma pedra")
print("Atras do mapa esta escrito \n\"A cada um destes locais a uma provação que so o guerreiro poderia completa-la\"")
print(f"O nome do guerreiro foi proclamado pela profecia .... {seu_nome} ....")