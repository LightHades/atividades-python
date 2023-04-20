salario = 1200

c1 = 200
c2 = 120

c1_com_taxa = c1 + (c1 * 0.02)
c2_com_taxa = c2 + (c2 * 0.02)

contas = c1_com_taxa + c2_com_taxa

print(f'João precisa pagar R$ {contas:.2f} de contas')