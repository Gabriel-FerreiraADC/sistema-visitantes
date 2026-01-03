saldo = float(input('Saldo: '))

cotacao_dolar = float(input('Dolar: '))

conversao = saldo / cotacao_dolar

print(f'Você tem R$ {saldo:.2f} e convertido para dolar $ {conversao:.2f}')