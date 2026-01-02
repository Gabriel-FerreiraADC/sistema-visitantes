while True:
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver saldo')
    print('4 - Sair')

    opcoes = input('ESCOLHA UMA OPÇÂO: ')

    if opcoes == '1':
        with open('banco.txt', 'a+') as arquivo:
            saldo = float(input('Valor á adicionar: '))
            arquivo.write(f'{saldo:.2f}\n')
            print(f'Saldo de R$ {saldo:.2f} adicionado')

    elif opcoes == '2':
        with open('banco.txt', 'a+') as arquivo:
            retirado = float(input('Valor a ser retirado: '))
            arquivo.write(f'-{retirado:.2f}\n')
            print(f'Saldo de R$ {retirado} retirado')

    
    elif opcoes == '3':
        try:
            with open('banco.txt', 'r') as arquivo:
                saldo_total = 0.0
                
                for linha in arquivo:
                    valor = float(linha.strip()) 
                    saldo_total = saldo_total + valor 
                
                print(f'Seu saldo total é de R$ {saldo_total:.2f}')
                
        except FileNotFoundError:
            print('Ainda não há movimentações na conta.')

    elif opcoes == '4':
        print('Sistema encerrado')
        break

    else:
        print('Opção inválida, tente de novo')