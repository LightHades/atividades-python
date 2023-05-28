numeros = []
numeros_impares = []

while True:
    try:
        n = int(input('Informe um número (cod de entrada: -999): '))
        
        if n != -999:
            numeros.append(n)
            if (n % 2 != 0):
                numeros_impares.append(n)
            else:
                continue
        else:
            break

    except KeyboardInterrupt:
        exit()

print(f'A quantidade de números ímpares informados é: {len(numeros_impares)}')