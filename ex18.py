valor_hora = float(input('Valor da hora: '))
horas = float(input('Horas trabalhadas: '))

salario_bruto = valor_hora * horas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = 0.1
elif salario_bruto > 2500:
    desconto_ir = 0.2

inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
ir = salario_bruto * desconto_ir
total_descontos = inss + ir
salario_liquido = (salario_bruto - total_descontos)

print(f'''
Salário Bruto ({valor_hora:.2f} * {horas:.0f}): R$ {salario_bruto:.2f}
\033[31m(-) IR ({desconto_ir * 100:.2f}%): R$ {ir:.2f}
(-) INSS (10%): R$ {inss:.2f}\033[0m
\033[32m(+) FGTS (11%): R$ {fgts:.2f}\033[0m
Total de descontos: R$ {total_descontos:.2f} 
Salário líquido: R$ {salario_liquido:.2f}
''')