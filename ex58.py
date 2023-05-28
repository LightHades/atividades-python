from time import sleep

menu = '''
1 - ( R$15,00 ) Bife acebolado
2 - ( R$25,00 ) Lasanha
3 - ( R$30,00 ) Filé mignon
4 - ( R$35,00 ) Salmão
5 - ( R$50,00 ) Caviar

0 - Sair
'''
preco = 0

while True:
    try:
        print(menu)
        prato = int(input('\nSelecione o prato >> '))
        if prato == 1:
            preco = 15
        elif prato == 2:
            preco = 25
        elif prato == 3:
            preco = 30
        elif prato == 4:
            preco = 35
        elif prato == 5:
            preco = 50
        elif prato == 0:
            break
        else:
            print('Selecine uma opção válida')

        taxa = input('\nDeseja pagar gorjeta de 10%? (s/n) >> ').lower()
        if taxa == 's':
            preco = (preco * 0.1) + preco

        print(f'\nO valor total a pagar é R${preco:.2f}')
        sleep(0.5)

        sair = input('Sair? (s/n) >> ')
        if sair == 's':
            break
        else:
            continue

    except ValueError:
        print('\nSelecione uma opção válida')
    except KeyboardInterrupt:
        print('\nSaindo...')
        break