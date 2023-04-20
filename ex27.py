lista = []

for i in range(1, 5):
    matricula = input('Matricula: ')
    sexo = input('Sexo (M / F): ').upper()
    altura = float(input('Altura (cm): '))
    status_fisico = int(input('Status fisico (1 - 3): '))
    print()

    aluno = {
        "matricula": matricula,
        "sexo": sexo,
        "altura": altura,
        "status_fisico": status_fisico
    }

    lista.append(aluno)

alunas_altas = [a for a in lista if a['altura'] > 170 and a['sexo'] == 'F']
qnt_alunas_altas = len(alunas_altas)

alunos = [h for h in lista if h['sexo'] == 'M']
qnt_alunos = len(alunos)
alunos_SF_bom = [sf_b for sf_b in lista if sf_b['status_fisico'] == 3]
qnt_alunos_SF_bom = len(alunos_SF_bom)
porcentagem_alunos_SF_bom = (qnt_alunos_SF_bom * 100) / qnt_alunos

print(f'Meninas maiores que 170 cm: {qnt_alunas_altas}')
print(f'Porcentagem de meinios com status fisico bom: {porcentagem_alunos_SF_bom:.0f}%')