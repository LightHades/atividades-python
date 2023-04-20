preco_inicial = float(input('Preco inicial do produto: '))

if preco_inicial < 50:
    preco = preco_inicial * 1.45
else:
    preco = preco_inicial * 1.3

print(f'O preco vendido no brecho é R${preco}')