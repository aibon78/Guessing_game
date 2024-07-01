import random




print("*********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativa = 0
pontos = 1000

chute =int(input("Digite o seu numero"))

if numero_secreto == chute:
    print("Você acertou")
else:
    print("Você errou")
    
if numero_secreto == chute:
    print("!!Muito bom!!")
else:
    print("Mandou mal")

if numero_secreto == chute:
    print("You Win")
else:
    print("Game Over")
    

