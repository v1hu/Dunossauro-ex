''''Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

print('''Qual turno você estuda? : 
[ M ] - MATUTINO
[ V ] - VESPERTINO
[ N ] - NOTURNO
''')

O = input('Sua opção: ').upper()

if O == 'M':
    print('Bom Dia!')
elif O == 'V':
    print('Boa Tarde!')
elif O == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

