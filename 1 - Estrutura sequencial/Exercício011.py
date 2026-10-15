
'''
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo. '''


X = int(input('Escolha um número Inteiro: '))
Y = int(input('Escolha outro número Inteiro: '))
R = float(input('Escolha um número Real: '))

print(f'O produto do dobro de {X} com a metade do {Y} é igual a : {(2*X) * (Y/2)}') # O produto do dobro do primeiro com metade do segundo
print(f'A soma do triplo de {X} com o {Y} é igual a : {(3*X)+R} ') # A soma do triplo do primeiro com o terceiro.
print(f'{R} elevado ao cubo é : {R**3}') # O terceiro elevado ao cubo.