litros = float(input("Litros vendidos"))
combustivel = input("Tipo de combustível (A-alcool / G-gasolina): ")

preco_alcool = 1.9
preco_gasolina = 2.5

if combustivel == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_sem_desconto = litros * preco_alcool
else:
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_sem_desconto = litros * preco_gasolina

valor_com_desconto = valor_sem_desconto * (1 - desconto)
print(f'Valor: R$ {valor_com_desconto:.2f}')