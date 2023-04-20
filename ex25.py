pequena_qnt = int(input('Quantidade de camisetas pequenas: '))
media_qnt = int(input('Quantidade de camisetas medias: '))
grande_qnt = int(input('Quantidade de camisetas grandes: '))

preco_pequena = pequena_qnt * 10
preco_media = media_qnt * 12
preco_grande = grande_qnt * 15

preco_total = preco_pequena + preco_media + preco_grande

print(f'O valor total da compra é R${preco_total}')