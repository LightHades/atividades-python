#!/usr/bin/python3

conta = input('Numero da conta: ')
saldo = float(input('Saldo: '))
debito = float(input('Debito: '))
credito = float(input('Credito: '))

saldo_atual = saldo - debito + credito

if saldo_atual > 0:
	print('Saldo positivo')
elif saldo_atual < 0:
	print('Saldo negativo')
else:
	print('Saldo nulo')
