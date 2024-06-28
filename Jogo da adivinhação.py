print("*********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("*********************************")

numero_secreto = 42

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
    

