"""'Faça um programa que peça dois números e imprima o maior deles."""

N1 = float(input("Digite um número: "))
N2 = float(input("Digite um número: "))

if N1 > N2:
    print(f"O valor {N1} é maior.")
elif N2 > N1:
    print(f"O valor de {N2} é maior. ")
elif N1 == N2:
    print(f'Os números são iguais.')