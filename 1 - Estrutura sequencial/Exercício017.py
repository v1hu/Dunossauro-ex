''''

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;

misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


'''

import math

area = float(input("Área a pintar em metros quadrados: "))

# Calcula a tinta necessária, incluindo 10% de folga
litros = area / 6 * 1.10

# Comprar somente latas
latas = math.ceil(litros / 18)
preco_latas = latas * 80

# Comprar somente galões
galoes = math.ceil(litros / 3.6)
preco_galoes = galoes * 25

# Misturar: usar latas primeiro e galões para completar
latas_mistura = int(litros / 18)
litros_faltando = litros - latas_mistura * 18
galoes_mistura = math.ceil(litros_faltando / 3.6)
preco_mistura = latas_mistura * 80 + galoes_mistura * 25

print("\nSomente latas:")
print("Latas:", latas)
print("Preço: R$", preco_latas)

print("\nSomente galões:")
print("Galões:", galoes)
print("Preço: R$", preco_galoes)

print("\nLatas e galões:")
print("Latas:", latas_mistura)
print("Galões:", galoes_mistura)
print("Preço: R$", preco_mistura)


'''
import math

area = float(input("Área a pintar em metros quadrados: "))

# Calcula a tinta necessária, incluindo 10% de folga
litros = area / 6 * 1.10

# Comprar somente latas
latas = math.ceil(litros / 18)
preco_latas = latas * 80

# Comprar somente galões
galoes = math.ceil(litros / 3.6)
preco_galoes = galoes * 25

# Misturar latas e galões
latas_mistura = int(litros / 18)
litros_faltando = litros - latas_mistura * 18

if litros_faltando > 0:
    galoes_mistura = math.ceil(litros_faltando / 3.6)
else:
    galoes_mistura = 0

preco_mistura = latas_mistura * 80 + galoes_mistura * 25

print("\nSomente latas:")
print("Latas:", latas)
print("Preço: R$", preco_latas)

print("\nSomente galões:")
print("Galões:", galoes)
print("Preço: R$", preco_galoes)

print("\nLatas e galões:")
print("Latas:", latas_mistura)
print("Galões:", galoes_mistura)
print("Preço: R$", preco_mistura) '''