print("Escolha uma opção:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

op = input("Digite o número correspondente à operação: ")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if op == '1':
    resultado = num1 + num2
elif op == '2':
    resultado = num1 - num2
elif op == '3':
    resultado = num1 * num2
elif op == '4':
    resultado = num1 / num2
else:
    print("Opção inválida!")

print(resultado)
if resultado % 2 == 0:
    print("O resultado é par")
else:
    print("O resultado é ímpar")

if resultado >= 0:
    print("O resultado é positivo")
else:
    print("O resultado é negativo")

if resultado.is_integer():
    print("O resultado é inteiro")
else:
    print("O resultado é decimal")