nome = input("Nome da pessoa: ")
sexo = input("Sexo da pessoa (M/F): ")
estado_civil = input("Estado civil da pessoa (solteiro/casado/divorciado/viuvo): ")

if sexo == "F" and estado_civil == "casado":
    tempo_casada = int(input("Tempo de casamento em anos: "))
    print(f"{nome} é casada há {tempo_casada} anos.")
else:
    print(f"{nome} é {sexo} e {'' if estado_civil == 'solteiro' else 'não é'} {estado_civil}.")
