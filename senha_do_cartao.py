senha_correta = 1234
tentativas = 0

while tentativas < 3:
    senha_usuario = int(input('Digite sua senha: '))
    if senha_usuario == senha_correta:
        print('Acesso liberado')
        break
    else:
        tentativas = tentativas + 1
        restante = 3 - tentativas

        if tentativas == 3:
            print('Limite de tentativas atingido CARTÃO BLOQUEADO')
            break
        else:
            print(f'Senha incorreta! você tem mais {restante} tentativas')

print('Retire o cartão')