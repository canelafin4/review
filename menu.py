import os

def menu_principal():
    print("O que deseja?")
    print("1- Escrever review de um filme")
    print("2- Escrever review de uma série")
    print("3- Mostrar minhas reviews de filmes")
    print("4- Mostrar minhas reviews de séries")
    print("0- Finalizar programa")


def limparTela():
    os.system('cls||clear')