ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_dias // 7

print(f"Idade em anos: {idade_anos}")
print(f"Idade em meses: {idade_meses}")
print(f"Idade em dias: {idade_dias}")
print(f"Idade em semanas: {idade_semanas}")