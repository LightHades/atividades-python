qnt_1 = int(input('Quantidade de modedas de 1 centavo: '))
qnt_5 = int(input('Quantidade de modedas de 5 centavos: '))
qnt_10 = int(input('Quantidade de modedas de 10 centavos: '))
qnt_25 = int(input('Quantidade de modedas de 25 centavos: '))
qnt_50 = int(input('Quantidade de modedas de 50 centavos: '))
qnt_1real = int(input('Quantidade de modedas de 1 real: '))

valor_em_real = (qnt_1 + (qnt_5 * 5) + (qnt_10 * 10) + (qnt_25 * 25) + (qnt_50 * 50) + (qnt_1real * 100)) / 100

print(f'O valor total em modeas é R$ {valor_em_real:.2f}')