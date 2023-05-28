cidades = []
veiculos = []
acidentes = []
for i in range(1, 6):
    cod_cidade = int(input('\nCodigo da cidade: '))
    n_veiculos = int(input('Número de veículos de passeio: '))
    n_acidentes = int(input('Número de acidentes de trânsito com vítimas: '))
    cidades.append(cod_cidade)
    veiculos.append(n_veiculos)
    acidentes.append(n_acidentes)

cidade_com_mais_acidentes = cidades[acidentes.index(max(acidentes))]
cidade_com_menos_acidentes = cidades[acidentes.index(min(acidentes))]
media_de_veiculos = sum(veiculos) / len(veiculos)
acidentes_menos_2000 = acidentes
for i in range(len(veiculos)-1, -1, -1):
    if veiculos[i] > 2000:
        acidentes_menos_2000.pop(i)
media_de_acidentes_cidades_com_menos_de_2000_veiculos = sum(acidentes_menos_2000) / len(acidentes_menos_2000)

print(f'''
Cidade com maior indice de acidentes: {cidade_com_mais_acidentes}. Indice: {max(acidentes)}
Cidade com menor indice de acidentes: {cidade_com_menos_acidentes}. Indice: {min(acidentes)}
Media de veículos nas cinco cidades juntas: {media_de_veiculos}
Media de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio: {media_de_acidentes_cidades_com_menos_de_2000_veiculos:.2f}
''')