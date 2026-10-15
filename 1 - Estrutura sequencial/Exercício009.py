# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Formula C = 5 * ((F-32) / 9).

F = float(input('Qual a temperatura: F° '))
print(f'A temperatura {F:.0f}°F transformado {5 * ((F-32) / 9):.0f}°C')