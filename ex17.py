#!/usr/bin/python3

salario = float(input('Salario: '))

if salario <= 280:
	percentual = '+ 20%'
	aumento = (salario * 0.2)
	novo = aumento + salario
elif salario > 280 and salario <= 700:
	percentual = '+ 15%'
	aumento = (salario * 0.15)
	novo = aumento + salario
elif salario > 700 and salario < 1500:
	percentual = '+ 10%'
	aumento = (salario * 0.1)
	novo = aumento + salario
elif salario >= 1500:
	percentual = '+ 5%'
	aumento = (salario * 0.05)
	novo = aumento + salario
	

print(f'Salario antigo: R$ {salario:.2f}')
print(f'Percentual: {percentual}')
print(f'Aumento: R$ {aumento:.2f}')
print(f'Novo salario: R$ {novo:.2f}')
