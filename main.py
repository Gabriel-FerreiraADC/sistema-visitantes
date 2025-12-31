with open('visitantes.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        nome = input("Nome: (Ou digite 'sair' para fechar)")
        if nome == 'sair':
            break
        documento = input('Documento: ')
        arquivo.write(f'{nome} - Documento: {documento}\n')
        print(f'Visitante cadastrado: {nome}')

print('Sistema Encerrado')