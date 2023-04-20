lista = []

for i in range(1, 4):
    lado = input(f'Lado {i}: ')
    lista.append(lado)

if len(set(lista)) == 1:
    triangulo = 'equilatero'

elif len(set(lista)) == 2:
    triangulo = 'isoceles'
else:
    triangulo = 'escaleno'

print(f'O triangulo é {triangulo}')