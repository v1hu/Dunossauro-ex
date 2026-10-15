''''

Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''
import math

M = float(input('Quantos M² área a ser pintada: '))

if M <= 54:
    print(f'Para {M:.2f}M² 1 lata de tinta é necessária, ela custa R$80,00')

else:

    print(f'Para {M:.0f}M² são necessárias {math.ceil(M/54):.0f} latas de tinta, no total de {math.ceil(M/54)*80:.2f}R$')




    '''

import math

area = float(input("Informe a área a ser pintada, em m²: "))

latas = math.ceil(area / 54)  # Cada lata cobre 18 × 3 = 54 m²
preco_total = latas * 80

print(f"Quantidade de latas: {latas}")
print(f"Preço total: R$ {preco_total:.2f}")

    '''