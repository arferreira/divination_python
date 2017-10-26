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

