import forca
import adivinhacao


def escolher_jogo():
    print("*********************************")
    print("******* Escolha seu jogo! *******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando advinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolher_jogo()
