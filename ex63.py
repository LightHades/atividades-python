qnt_numeros = int(input('Quantidade de numeros: '))
lista = []
for i in range(1, qnt_numeros + 1):
    n = int(input(f'Numero {i}: '))
    lista.append(n)
print(f'Maior numero: {max(lista)}\nMenor numero: {min(lista)}\nSoma de todos: {sum(lista)}')