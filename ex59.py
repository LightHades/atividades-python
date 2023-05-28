n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
lista = []

while n1 > n2:
    n2 += 1
    lista.append(n2)

while n2 > n1:
    n1 += 1
    lista.append(n1)

lista.pop()

print(lista)