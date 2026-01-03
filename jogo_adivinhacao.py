numero_certo = 7
tentativas = 0

while tentativas < 5:
    chutes = int(input('Digite um número de 0 a 10: '))

    if chutes == numero_certo:
        print('Você acertou o número! Parabéns')
        break
    else:
        tentativas = tentativas + 1
        chances = tentativas
        print(f'Você tem 5 chances para acertar!')
        print(f'Você tentou {chances} vezes')
        if chances == 5:
            print('Limite de chances atingido (GAME OVER)')

print('OBRIGADO POR JOGAR')