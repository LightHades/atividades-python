salario_fixo = float(input('Salário fixo: R$ '))
valor_venda = float(input('Valor da venda: R$ '))
qnt_vendas = int(input('Quantidade de vendas: '))

salario_final = salario_fixo + ((valor_venda * 0.04) * qnt_vendas)

print(f'Salário final: R$ {salario_final}')