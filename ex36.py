print('''Cachorro Quente 100 R$ 11,20
101 - Ovo Simples R$ 8,30
102 - Bauru com Ovo R$ 11,50
103 - Hambúrguer R$ 16,20
201 - Refrigerante R$ 6,00
202 - Suco R$ 7,50
203 - Água Mineral R$ 4,70
''')

lanche = int(input('Lanche: '))
bebida = int(input('Bebida: '))

preco_lanche = 0
preco_bebida = 0

if lanche == 101:
    preco_lanche = 8.3
elif lanche == 102:
    preco_lanche = 11.5
elif lanche == 103:
    preco_lanche = 16.2
else:
    print('Insira um lanche válido')

if bebida == 201:
    preco_bebida = 6
elif bebida == 202:
    preco_bebida = 7.5
elif bebida == 203:
    preco_bebida = 4.7
else:
    print('Insira uma bebida válida')

valor = preco_lanche + preco_bebida
print(f'O valor total foi R$ {valor:.2f}')