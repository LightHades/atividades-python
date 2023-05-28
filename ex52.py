numeros = []

while True:
    try:
        n = int(input('Informe um número (cod de entrada: -1): '))
        
        if n != -1:
            numeros.append(n)
        else:
            break

    except KeyboardInterrupt:
        exit()

print(f'A quantidade de números informados é: {len(numeros)}')