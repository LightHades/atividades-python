numeros = []
cont = 1

while cont <= 20:
    try:
        n = int(input('Informe um número: '))
        numeros.append(n)
        cont += 1

    except KeyboardInterrupt:
        exit()

print(f'O maior número informado é {max(numeros)}\nO menor número informado é: {min(numeros)}')