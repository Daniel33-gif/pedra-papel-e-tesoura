import random

print ("seja bem vindo ao jogo")

print ("suas escolhas sao pedra,papel ou tesoura")

escolha_jogador = input("faça sua escolha:")

possibilidades = ("pedra" , "papel" , "tesoura")

escolha_computador = random.choice(possibilidades)

print (escolha_computador)

if escolha_computador == escolha_jogador:
    print ("empate")
elif escolha_jogador  == "pedra" and  escolha_computador== "tesoura":
    print ("vc ganhou")
elif escolha_jogador == "pedra" and  escolha_computador == "papel":
    print ("o computador ganhou")
elif escolha_jogador == "papel" and  escolha_computador == "pedra":
    print ("vc ganhou")
elif escolha_jogador == "papel" and  escolha_computador == "tesoura":
    print ("o computador ganhou")
elif escolha_jogador == "tesoura" and  escolha_computador == "pedra":
    print ("o computador ganhou")
elif escolha_jogador == "tesoura" and  escolha_computador == "papel":
    print ("o você ganhou")