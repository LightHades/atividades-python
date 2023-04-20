lata = 350
garrafa_600 = 600
garrafa_2l = 2000

def converter_ML_L(mililitro):
    convertido = mililitro / 1000
    return convertido

lata = converter_ML_L(lata)
garrafa_600 = converter_ML_L(garrafa_600)
garrafa_2l = converter_ML_L(garrafa_2l)

total = lata + garrafa_600 + garrafa_2l

print(f'Total de litros: {total} L')