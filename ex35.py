print('''
1 - File Duplo
2 - Alcatra
3 - Picanha
''')
desconto = 0
tipo_carne = int(input("Tipo de carne: "))
quantidade = float(input("Quantidade em Kg: "))
forma_pagamento = input("Forma de pagamento (Dinheiro / Cartão): ").lower()

if tipo_carne == 1:
    if quantidade <= 5:
        preco_total = quantidade * 34.90
    else:
        preco_total = quantidade * 35.80
    carne = "File Duplo"
elif tipo_carne == 2:
    if quantidade <= 5:
        preco_total = quantidade * 44.90
    else:
        preco_total = quantidade * 46.80
    carne = "Alcatra"
elif tipo_carne == 3:
    if quantidade <= 5:
        preco_total = quantidade * 66.90
    else:
        preco_total = quantidade * 67.80
    carne = "Picanha"
else:
    print("Opção inválida. Por favor, escolha um número entre 1 e 3.")
    exit()

if forma_pagamento == "cartão":
    desconto = preco_total * 0.05

valor_a_pagar = preco_total - desconto

print(f'''
Tipo de carne: {carne}
Quantidade: {quantidade:.2f} Kg
Preço total: R${preco_total:.2f}
Forma de pagamento: {forma_pagamento}
Desconto: R${desconto:.2f}
Valor a pagar: R${valor_a_pagar:.2f}
''')