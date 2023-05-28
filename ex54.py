numeros = []
numeros_50 = []

while True:
    try:
        n = int(input('Informe um número (cod de entrada: 0): '))
        
        if n != 0:
            numeros.append(n)
            if (n == 50):
                numeros_50.append(n)
            else:
                continue
        else:
            break

    except KeyboardInterrupt:
        exit()

print(f'A quantidade de números "50" informados é: {len(numeros_50)}')