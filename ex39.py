data = input('Data (dd/mm): ')

dia = int(data[:2])
mes = int(data[3:])

qnt_meses = mes - 1
qnt_dias = (qnt_meses * 30) + dia

print(f'Se passaram {qnt_dias} dias desde o começo do ano')