#!/usr/bin/python3

nome = input('Seu nome: ')
idade = int(input('Sua idade: '))

if idade >= 0 and idade <= 2:
	tipo = 'bebe'
elif idade >=3 and idade <= 11:
	tipo = 'crianca'
elif idade >= 12 and idade <= 21:
	tipo = 'jovem'
elif idade >= 22 and idade <= 64:
	tipo = 'adulto'
elif idade >= 65 and idade <= 100:
	tipo = 'velhinho'
elif idade >= 101:
	tipo = 'muito velhinho'
else:
	print('Favor insira uma idade coerente')

print(f'{nome} esta com {idade} e e considarado {tipo}')
