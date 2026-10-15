''' Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

'''
#8x30 = mes = 240
#60/8= 7.5


H = float(input('Qual o valor da hora trabalhada?\n'))
M = float(input('Quantas horas trabalhadas no mês?\n'))

print(f'O valor do salário bruto no mês é : R${H*M:.2f}\n')
print(f'O valor do salário após o desconto do IR (11%): R${(H*M)*0.11:.2f}\n')
print(f'O valor do salário após desconto de INSS (8%): R${(H*M)*0.08:.2f} \n')
print(f'O valor do salário após do desconto do Sindicato (5%): R${(H*M)*0.05:.2f} \n')
print(f'O valor do salário Liquido é : R${(H*M)-(H*M*0.11)-(H*M*0.08)-(H*M*0.05):.2f}\n')