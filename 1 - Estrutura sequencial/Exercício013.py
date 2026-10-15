''''

Tendo como dados de entrada um arquivo em Gigabytes, 
construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

'''

G = float(input('Qual valor do arquivo em GBs: '))
print(f'O valor em Megabytes é : { G * 1024 }Mbs ')
print(f'O valor em Kilobytes é : { G * (1024**2) }Kbs ')
print(f'O valor em Bytes é : { G * (1024**3) }Bs ')