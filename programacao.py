while True:
    print('\n--- MENU DE TAREFAS ---')
    print('1 - Adicionar Tarefa')
    print('2 - Ver Lista')
    print('3 - Sair')
    print('4 - Apagar lista')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        with open('tarefa.txt', 'a', encoding='utf-8') as arquivo:
            nova_tarefa = input('Qual tarefa você quer adicionar: ')
            arquivo.write(f'{nova_tarefa}\n')
            print('TAREFA ANOTADA')
    
    elif opcao == '2':
        with open('tarefa.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                print(linha.strip())
        
    elif opcao == '3':
        print('Saindo...')
        break

    elif opcao == '4':
        with open('tarefa.txt', 'w') as arquivo:
            print('Lista apagada')
    
    else:
        print('Opção inválida, tente de novo.')

print('SISTEMA ENCERRADO')