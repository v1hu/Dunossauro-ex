''''

Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


'''

M = float(input('Qual o tamanho do arquivo? ')) # megabyts por segundo = 1byte = 8bits = transformar MB para MBPs = X*8
print(f'{M:g} MB')

V = float(input('Qual a velocidade da internet ? Mbps'))
print(f'{V:g} Mbps')

print(f'O tempo aproximado de download do arquivo é {int(((M*8)/V)//60)} minutos e {int(((M*8)/V)%60)} segundos.')