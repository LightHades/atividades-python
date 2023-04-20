kg = float(input('Peso do peixe: '))

if kg > 50:
    excesso = kg - 50
    multa = excesso * 4
    
    print(f'KGs excedidos: {excesso:.1f}')
    print(f'Multa: R$ {multa:.2f}')

else:
    print('Sem problemas')