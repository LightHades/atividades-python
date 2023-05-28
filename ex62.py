numero = int(input("Digite um número inteiro: "))

fatorial = 1
expressao = str(numero) + "! = "

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0 or numero == 1:
    print(f"{expressao}1 = 1")
else:
    for i in range(2, numero + 1):
        fatorial *= i
        expressao += str(i) + "."

    expressao = expressao[:-1]  # Remove o último ponto
    expressao += " = " + str(fatorial)
    print(expressao)