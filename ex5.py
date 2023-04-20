nome = input("Nome do aluno: ")
disciplina = input("Disciplina: ")
prova1 = float(input("Primeira nota: "))
prova2 = float(input("Segunda nota: "))
prova3 = float(input("Terceira nota: "))

media = (prova1 + prova2 + prova3) / 3

print(f"\nMédia: {media:.2}")