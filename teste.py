veiculos = [700, 3000, 400]
acidentes = [10, 16, 6]
acidentes_novo = acidentes

lista = [1500, 2500, 1800, 3000, 2200, 2100]

for i in range(len(veiculos)-1, -1, -1):
    if veiculos[i] > 2000:
        veiculos.pop(i)
        acidentes.pop(i)

print("Veiculos:", veiculos)
print("Acidentes:", acidentes)




# cidade_com_mais_acidentes = cidades[acidentes.index(max(acidentes))]