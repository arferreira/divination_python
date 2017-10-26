# function sort
from random import randint


def welcome():
    print("Bem-vindo ao jogo da adivinhação.")
    print("\n\n")
    name = input("Qual o seu nome? ")
    print("\n\n")
    print("Começaremos o jogo para você, {}".format(name))


def sort():
    print("\n\n")
    print("Escolhendo um número secreto entre 0 e 200...")
    number_secret = randint(0,200)
    print("Escolhido ... Que tal adivinhar hoje nosso número secreto?")
    return number_secret

def get_number(kicks, attempt, limit):
    print("\n\n\n")
    print("Tentativa {} de {}.".format(attempt, limit))
    print("Chutes atá agora: {}".format(kicks))
    kick = int(input("Escolha um número: "))
    print("Será que você acertou?? Você escolheu o número: {}".format(kick))
    return kick

def verify(kick, number_secret):
    if kick == number_secret:
        print("Parabéns!!! Você acertou!")
        return True
    else:
        print("Humm.. Você errou!")
        larger = number_secret > kick
        if larger:
            print("O número secreto é maior!")
        else:
            print("O número secreto é menor!")
        return False

welcome()

number_secret = sort()

i = 1

limit = 10

kicks = []


while i <= limit:
    kick = get_number(kicks, i, limit)
    kicks.append(kick)
    if verify(kick, number_secret):
        break
    i += 1


