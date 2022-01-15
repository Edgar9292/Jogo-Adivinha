import random
def gera():
    return random.randint(0,100)

def game():
    resposta = gera()
    tentativa =0
    print("\nAqui vem o palpite")

    palpite=0
    while palpite is not resposta:
        tentativa +=1
        palpite = int(input(" Digite seu palpite?"))
        if palpite > resposta:
            print("Incorreto!É um valor menor que", palpite)
        elif palpite < resposta:
            print("Incorreto!é um valor maior que", palpite)
        else:
            print("Parabéns! AEEEE!!!!!! O número gerado foi", resposta, "E você acertou em", tentativa, "tentativas!")

while True:
    game()

