qnt_paes = int(input('Quantidade de pães: '))
qnt_broas = int(input('Quantidade de broas: '))

valor_paes = qnt_paes * 1
valor_broas = qnt_broas * 3.5

total = valor_paes + valor_broas

poupanca = total * 0.1

lucro_liquido = total - poupanca

print(f'Total arrecadado: R$ {total:.2f}')
print(f'Quantidade na poupança: R$ {poupanca:.2f}')
print(f'Valor liquido final: R$ {lucro_liquido:.2f}')