# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (C * 9/5) + 32

C = float(input('Qual a temperatura: C° '))
print(f'A temperatura {C:.0f}°C transformado {(C * 9/5) + 32:.0f}°F')