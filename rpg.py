#    variaveis globais    #
racas = ["humano", "elfo", "anão", "draconico"]
locais = ["cidade", "floresta", "minas"]
armas_iniciais = ["espada", "arco", "martelo"]
dano_inicial = [""]
inimigos_habitantes = ["ladrão", "slime", "morcegos"]

seu_nome = "a"
sua_raça = "b"

slot_arma = ""
slot_1 = ""
slot_2 = ""
slot_3 = ""




#    defs (oque faz o jogo rodar)    #
def acordou():
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
            print("Não ouve uma escolha valida \n")


acordou()
print (f"\nseu nome é {seu_nome}, e você é um {racas[sua_raça]}")
print ()