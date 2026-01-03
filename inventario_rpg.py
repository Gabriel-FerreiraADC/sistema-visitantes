inventario = []


while True:
    item = input('Qual o nome do item: (Ou digite "FIM" para sair)')
    if item.upper() == 'FIM':
        break
    else:
        inventario.append(item)
        print(f'Item {item} adicionado')

print(inventario)
itens_total = len(inventario)
print(f'Total de itens: {itens_total}')