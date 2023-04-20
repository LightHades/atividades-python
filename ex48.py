preco = float(input("Preço do produto: R$"))
pagamento = int(input("1 - à vista em dinheiro ou pix\n2 - à vista no cartão de crédito\n3 - em duas vezes\n4 - em três vezes: "))

if pagamento == 1:
    preco_final = preco * 0.9
elif pagamento == 2:
    preco_final = preco * 0.95
elif pagamento == 3:
    preco_final = preco
    parcelas = preco_final / 2
    print(f"O valor de cada parcela é de R${parcelas:.2f}")
elif pagamento == 4:
    preco_final = preco * 1.1
    parcelas = preco_final / 3
    print(f"O valor de cada parcela é de R${parcelas:.2f}")
else:
    preco_final = preco
    print("Condição de pagamento inválida!")

if pagamento in [1, 2, 3, 4]:
    print(f"O valor final do produto é de R${preco_final:.2f}")
