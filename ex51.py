numeros = []

while True:
    try:
        n = int(input('Informe um número (cod de entrada: -999): '))
        
        if n != -999:
            numeros.append(n)
        else:
            break

    except KeyboardInterrupt:
        exit()

print(f'A soma dos números informados é: {sum(numeros)}')