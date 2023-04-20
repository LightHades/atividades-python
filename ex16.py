#!/usr/bin/python3

lista = []
for i in range(0, 3):
	n = int(input('>>> '))
	lista.append(n)

maior = max(lista)
menor = min(lista)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
