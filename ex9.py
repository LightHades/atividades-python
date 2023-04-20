
nome = input("Nome do aluno: ")
disciplina = input("Disciplina: ")
prova1 = float(input("Primeira nota: "))
prova2 = float(input("Segunda nota: "))
prova3 = float(input("Terceira nota: "))

media = (prova1 + prova2 + prova3) / 3

print(f"Média: {media:.2}")

if media >= 6:
    print(f"\nO aluno(a) {nome} foi aprovado(a)!")

else:
    print(f"\nO aluno(a) {nome} foi reprovado(a)")
