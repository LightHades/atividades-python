n1_int = int(input('Primeiro numero inteiro: '))
n2_int = int(input('Segundo numero inteiro: '))
n_real = float(input('Numero real: '))

dobro_n1_int = n1_int * 2
metade_n2_int = n2_int / 2

triplo_n1_int = n1_int * 3

terceiro_cubo = n_real * n_real * n_real

print(f'''
O produto do dobro do primeiro com metade do segundo: {dobro_n1_int * metade_n2_int:.2f}
A soma do triplo do primeiro com o terceiro: {triplo_n1_int + n_real:.2f}
O terceiro elevado ao cubo: {terceiro_cubo:.2f}''')