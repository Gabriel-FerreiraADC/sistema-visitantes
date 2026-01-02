while True:
    print('\n=== SISTEMA BANCÁRIO ===')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver saldo')
    print('4 - Sair')

    opcoes = input('ESCOLHA UMA OPÇÃO: ')

    if opcoes == '1':
        with open('banco.txt', 'a+') as arquivo:
            valor_deposito = float(input('Valor a adicionar: '))
            arquivo.write(f'{valor_deposito:.2f}\n')
            print(f'Sucesso! R$ {valor_deposito:.2f} adicionado.')

    elif opcoes == '2':
        saldo_atual = 0.0
        try:
            with open('banco.txt', 'r') as arquivo:
                for linha in arquivo:
                    valor = float(linha.strip())
                    saldo_atual = saldo_atual + valor
        except FileNotFoundError:
            saldo_atual = 0.0

        print(f'(Seu saldo disponível é: R$ {saldo_atual:.2f})')
        valor_saque = float(input('Valor a ser retirado: '))

        if valor_saque <= saldo_atual:
            
            with open('banco.txt', 'a+') as arquivo:
                arquivo.write(f'-{valor_saque:.2f}\n')
            print(f'Saque de R$ {valor_saque:.2f} realizado!')
        else:
            print('NEGADO: Saldo Insuficiente.')

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
        print('Sistema encerrado.')
        break

    else:
        print('Opção inválida, tente de novo.')