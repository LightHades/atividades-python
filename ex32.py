saque = int(input('Valor do saque (R$10 - R$600): '))

if saque >= 10 and saque <= 600:
    qnt_notas_100 = saque // 100
    saque = saque % 100
    qnt_notas_50 = saque // 50
    saque = saque % 50
    qnt_notas_10 = saque // 10
    saque = saque % 10
    qnt_notas_5 = saque // 5
    saque = saque % 5
    qnt_notas_1 = saque // 1
    saque = saque % 1
    
    print(f'''
Quantidade de notas de 100: {qnt_notas_100}
Quantidade de notas de 50: {qnt_notas_50}
Quantidade de notas de 10: {qnt_notas_10}
Quantidade de notas de 5: {qnt_notas_5}
Quantidade de notas de 1: {qnt_notas_1}''')

else:
    print('Valor invalido')