"""Faça um programa que peça um valor e mostre na tela se o valor é positivo, negativo ou neutro."""

n = float(input("Digite um número: "))

if n > 0:
    print(f"O número {n} é positivo.")
elif n < 0:
    print(f"O número {n} é negativo.")
else:
    print(f"O número {n} é neutro.")
