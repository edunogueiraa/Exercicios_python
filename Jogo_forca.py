import getpass

def jogar():
    print()
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************\n")

    print("ATENÇÃO!!!")
    tema = input("Digite o tema do jogo da forca: ")
    palavra_secreta = getpass.getpass("Digite a palavra secreta para seu amigo jogar: ")
    palavra_secreta = palavra_secreta.upper()  # Atribua o resultado de .upper() de volta a palavra_secreta

    letra_dica = ["_"] * len(palavra_secreta)

    print("_____________" + tema + "_____________\n")
    print(" ".join(letra_dica))
    print("Possui 6 tentativas. \n")

    nao_inforcou = True
    tentativas = 6
    letras_usadas = []

    while nao_inforcou:
        chute = input("Digite uma letra: \n")
        chute = chute.strip().upper()

        if chute in letras_usadas:
            print("Você já tentou esta letra. Tente outra.")

        letras_usadas.append(chute)

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letra_dica[index] = letra
                index += 1
        else:
            print("Letra errada! \n")
            tentativas -= 1

        print(" ".join(letra_dica))

        if "_" not in letra_dica:
            print("Parabéns!!! Você acertou a palavra secreta. \n")
            nao_inforcou = False
        elif tentativas == 0:
            print("Você se enforcou. A palavra secreta era: ", palavra_secreta)
            nao_inforcou = False
        else:
            print("___________Continue jogando _________\n")

    print("Fim do jogo!")

if __name__ == '__main__':
    jogar()
