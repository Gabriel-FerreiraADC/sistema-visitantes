limite_emprestimo = 0.50

salario = float(input('Salário: '))
valor_emprestimo = float(input('Valor empréstimo: '))

if valor_emprestimo <= salario * limite_emprestimo:
    print('Parabéns, seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado')