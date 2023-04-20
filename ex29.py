altura = float(input('Altura (m): '))

peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7

print(f'''
Peso ideal homens: {peso_ideal_h:.2f} kg
Peso ideal mulheres: {peso_ideal_m:.2f} kg''')