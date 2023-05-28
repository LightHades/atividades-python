pares = []
impares = []

while True:
    try:
        for i in range(1, 11):
            n = int(input(f'Numero {i}: '))
            if n % 2:
                impares.append(n)
            else:
                pares.append(n)

        print(f'Numeros pares: {len(pares)}\nNumeros impares: {len(impares)}')
        break

    except KeyboardInterrupt:
        exit()
