''''Faça um programa que leia três números e mostre o maior deles:'''

N1 = float(input("Digite um número: "))
N2 = float(input("Digite um número: "))
N3 = float(input("Digite um número: "))

if N1 > N2 and N1 > N3:
    print(f"O valor {N1} é maior.")
elif N2 > N1 and N2 > N3:
    print(f"O valor de {N2} é maior. ")
elif N3 > N1 and N3 > N2:
    print(f'O valor de {N3} é maior.')
else:
    print('Os números são iguais.')