''''Faça um programa para a leitura de duas notas parciais de um aluno. '
O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

N1 = float(input('Nota da P1: '))
N2 = float(input('Nota da P2: '))

M = (N1 + N2) / 2

if M < 7:
    print(f'Sua média foi {M:.2f}, REPROVADO!')

elif M >= 7 and M <= 9:
    print(f'Sua média foi {M:.2f},APROVADO!')

elif M == 10:
    print(f'Sua média foi {M:.2f}, APROVADO COM DISTINÇÃO')